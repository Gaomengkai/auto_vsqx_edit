# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import pinyin2xsampa
#pinyin2xsampa from GitHub: https://github.com/m13253/pinyin2xsampa.git
'''
Copyright (C) 2018  Gao Mengkai <gaomengkai0@outlook.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
debug=True
namespace="{http://www.yamaha.co.jp/vocaloid/schema/vsq4/}"

def cdata_a_string(string):
    temp="@12@{}@13@".format(string)
    return temp

class vsqx_option():
    def __init__(self,data,path=None):
        self.notes=[]
        self.path=path
        self.data=data
        self.phonetic=[]
        self.number=0
        self.lrc=[]
    def start_doing(self):
        ET.register_namespace('',"http://www.yamaha.co.jp/vocaloid/schema/vsq4/")
        ET.register_namespace('xsi',"http://www.w3.org/2001/XMLSchema-instance")
        namespace="{http://www.yamaha.co.jp/vocaloid/schema/vsq4/}"
        if self.path == None:
            self.root=ET.fromstring(self.data)
            tree=self.root
        else:
            self.tree=ET.parse(self.path)
            self.root=self.tree.getroot()
            tree=self.tree
        self.singers=tree.find('./%svVoiceTable'%namespace).findall('%svVoice'%namespace)
        s_bs=[];s_pc=[];s_name=[]
        for singer in self.singers:
            s_bs.append(singer.find('%sbs'%namespace).text)
            s_pc.append(singer.find('%spc'%namespace).text)
            s_name.append(singer.find('%sname'%namespace).text.replace('@12@','').replace('@13@',''))
        self.tracks=tree.findall('./%svsTrack'%namespace)
        print("[+] "+str(len(self.tracks))+" tracks were found")
        trackN=0
        for track in self.tracks:
            print()
            print("[+] "+str(trackN))
            print("[-] Name    ="+track.find('%sname'%namespace).text.replace('@12@','').replace('@13@',''))
            print("[-] Comment ="+track.find('%scomment'%namespace).text.replace('@12@','').replace('@13@',''))
            trackN+=1
        print()
        try:
            chose_track=self.tracks[int(input("Choose the track: "))]
        except Exception:
            print("[!] ERROR No such part!\nNo.0 part was selected.")
            chose_track=self.tracks[0]

        print()
        self.parts=chose_track.findall('./%svsPart'%namespace)
        print("[+] "+str(len(self.parts))+" parts were found")
        partN=0
        for part in self.parts:
            print()
            print("[+] "+str(partN))
            print("[-] Name    ="+part.find('%sname'%namespace).text.replace('@12@','').replace('@13@',''))
            print("[-] Comment ="+part.find('%scomment'%namespace).text.replace('@12@','').replace('@13@',''))
            for i in range(len(s_pc)):
                if part.find('%ssinger'%namespace).find('%spc'%namespace).text == s_pc[i]:
                    print("[-] Singer  ="+s_name[i])
            partN+=1
        print()
        try:
            chose_part=self.parts[int(input("Choose the part: "))]
        except Exception:
            print("[!] ERROR No such part!\nNo.0 part was selected.")
            chose_part=self.parts[0]

        self.notes=chose_part.findall('./%snote'%namespace)
        #self.notes=tree.findall('./%svsTrack/%svsPart/%snote'%(namespace,namespace,namespace))
        noteN=0
        print("[+] "+str(len(self.notes))+" notes were found")
        for note in self.notes:
            #self.lrc.append(note.find('%sy'%namespace).text)
            #self.phonetic.append(note.find('%sp'%namespace).text)
            print()
            #print("[+] "+str(noteN))
            #print("[-] Lyric    ="+note.find('%sy'%namespace).text.replace('@12@','').replace('@13@',''))
            #print("[-] Phonetic ="+note.find('%sp'%namespace).text.replace('@12@','').replace('@13@',''))
            #print("[-] Location ="+note.find('%st'%namespace).text)
            #print("[-] Length   ="+note.find('%sdur'%namespace).text)
            #print("[-] Tone     ="+note.find('%sn'%namespace).text)
            #print("[-] VEL      ="+note.find('%sv'%namespace).text)
            #Code above is so long...
            printstr = "[" + str(noteN) +']'+'LRC='+note.find('%sy'%namespace).text.replace('@12@','').replace('@13@','')
            printstr += "\nPHONETIC="+note.find('%sp'%namespace).text.replace('@12@','').replace('@13@','')
            printstr += "\nLOCATION="+note.find('%st'%namespace).text.replace('@12@','').replace('@13@','')
            print(printstr)
            noteN+=1
        return chose_part

    
    def append_note(self,element_path,location,lrc,phonetic,vel=64,length=480,tone=72,accent=80,
            bendDep=8,bendLen=0,decay=70,fallPort=0,opening=127,
            risePort=0,vibLen=66,vibType=1,path="./%svsTrack/%svsPart"%(namespace,namespace),):
        if(element_path == None):
            #Default Option
            vsPart=self.root.findall(path)
            leng=len(vsPart)
            vsPart=vsPart[leng-1]
            if debug:
                print(vsPart)
        else:
            vsPart=element_path
        #Starting creating nodes
        vsPart.remove(vsPart.find('%splane'%namespace))#remove PLANE tag
        note=ET.SubElement(vsPart,'note')#Creative tags
        t=ET.SubElement(note,'t')
        dur=ET.SubElement(note,'dur')
        n=ET.SubElement(note,'n')
        v=ET.SubElement(note,'v')
        y=ET.SubElement(note,'y')
        p=ET.SubElement(note,'p')
        nStyle=ET.SubElement(note,'nStyle')
        nStyles=['accent','bendDep','bendLen','decay','fallPort',
            'opening','risePort','vibLen','vibType']
        ns=[]
        opts=[accent,bendDep,bendLen,decay,fallPort,
            opening,risePort,vibLen,vibType]#Advanced Options
        for i in range(0,len(nStyles)):
            temp=ET.SubElement(nStyle,'v')
            temp.attrib['id']=str(nStyles[i])
            temp.text=str(opts[i])
            ns.append(temp)
        vd=ET.SubElement(nStyle,'seq')
        vd.attrib['id']='vibDep'
        vr=ET.SubElement(nStyle,'seq')
        vr.attrib['id']='vibRate'
        cc1=ET.SubElement(vd,'cc')
        p1=ET.SubElement(cc1,'p')
        p1.text='22391'
        v1=ET.SubElement(cc1,'v')
        v1.text='64'
        cc1=ET.SubElement(vr,'cc')
        p1=ET.SubElement(cc1,'p')
        p1.text='22391'
        v1=ET.SubElement(cc1,'v')
        v1.text='64'
        #Ending creating nodes

        #Writing data
        t.text=str(location)
        dur.text=str(length)
        n.text=str(tone)
        v.text=str(vel)
        y.text=cdata_a_string(lrc)
        p.text=cdata_a_string(phonetic)
        plane=ET.SubElement(vsPart,'plane')
        plane.text='0'
    def save_vsqx(self,path=None,outString=True):
        if outString:
            return ET.tostring(self.root,encoding='utf-8')
        else:
            self.tree.write(path,'utf-8',True)
    def incept_phonetic(self,selected_part,phonetic,begin=0,end=None):
        part=selected_part
        notes=part.findall('./%snote'%namespace)
        if end is None:
            end=begin+len(phonetic)-1
        if end >= len(notes):
            print("[!] The phonetics are too much!\n    And the phonetics out of range will be delect.")
            decision=input("Do you want to go ahead?[y/n]")
            if decision not in ['y','Y']:
                return False
            end=len(notes)-1
        for i in range(begin,end+1):
            p=phonetic[i-begin]
            if p is '':
                continue
            note=notes[i].find('./%sp'%namespace)
            note.text=cdata_a_string(p)
            print("{}:is added as {}".format(i-begin,p))
        return True
    def change_note(self,note,t=None,dur=None,n=None,v=None,y=None,p=None,nStyles=None):
        if t is not None:
            note.find('./%st'%namespace).text=str(t)
        if dur is not None:
            note.find('./%sdur'%namespace).text=str(dur)
        if n is not None:
            note.find('./%sn'%namespace).text=str(n)
        if v is not None:
            note.find('./%sv'%namespace).text=str(v)
        if y is not None:
            note.find('./%sy'%namespace).text=str(y)
        if p is not None:
            note.find('./%sp'%namespace).text=str(p)
        if nStyles is not None and len(nStyles) is 9:
            ns=note.find('./%snStyles'%namespace)
            for i in range(len(nStyles)):
                if i is not None:
                    ns[i].text=str(nStyles[i])
                    #BUG HERE
        return note
        
        
def preprocess(data):
    data=data.replace('<![CDATA[','@12@')
    data=data.replace(']]>','@13@')
    return data
def endprocess(data):
    data=data.replace('@12@','<![CDATA[')
    data=data.replace('@13@',']]>')
    will_write="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>"""+data
    return will_write
def interface(path=None):
    if path is not None:
        dat=open(path).read()
    while path is None:
        print("Open a file:")
        path=input()
        if(path!=None):
            try:
                dat=open(path).read()
            except Exception as e:
                print(e)
                print("[-] File opening error.")
                path=None
                continue
            break
    dat=preprocess(dat)
    choice='1'
    isFirst=True
    while True:
        print()
        print("Pleace choose the mode you want to get in:")
        print("1. Read a vsqx file standard or reselect part")
        print("2. Phonetic inception")
        print("3. Append note  //TESTING")
        print("4. Refresh v tree")
        print("5. Edit a note")
        print("9. Save the vsqx file")
        print("0. Quit")
        if isFirst:
            v=vsqx_option(data=dat)
            part=False
        choice=input("Your choice:")
        if choice is '0':
            return
        if choice not in ['1','2','9','4','5']:
            continue
        if choice is '4':
            v=vsqx_option(data=dat)
            part=v.start_doing()
        if choice is '9' and part:
            interface_9(v,path)
        elif choice is '9':
            part=v.start_doing()
            interface_9(v,path)
        if isFirst:
            isFirst=False
            part=v.start_doing()
        if choice is '1':
            pass
        if choice is '2':
            interface_2(v,part)
        if choice is '5':
            interface_5(v,part)
def interface_5(vocaloid,part):
    num = int(input("Enter the number of a note:"))
    notes=part.findall('./%snote'%namespace)
    note = notes[num]
    #def change_note(self,note,t=None,dur=None,n=None,v=None,y=None,p=None,nStyles=None)
    print("[-] Lyric    ="+note.find('%sy'%namespace).text.replace('@12@','').replace('@13@',''))
    print("[-] Phonetic ="+note.find('%sp'%namespace).text.replace('@12@','').replace('@13@',''))
    print("[-] Location ="+note.find('%st'%namespace).text)
    print("[-] Length   ="+note.find('%sdur'%namespace).text)
    print("[-] Tone     ="+note.find('%sn'%namespace).text)
    print("[-] VEL      ="+note.find('%sv'%namespace).text)
    print("[-] OPE      ="+note.find('%snStyle'%namespace).findall("./%sv"%namespace)[5].text)

    y=input("Edit Lrc:")
    p=input("Edit Phonetic:")
    t=input("Edit Location:")
    dur=input("Edit Length:")
    n=input("Edit Tone:")
    v=input("Edit VEL:")
    if y is '':
        y = None
    if p is '':
        p = None
    if t is '':
        t = None
    else:
        t=int(t)
    if dur is '':
        dur = None
    else:
        dur=int(dur)
    if n is '':
        n = None
    else:
        n=int(n)
    if v is '':
        v = None
    else:
        v=int(v)
    ope=input("Edit OPE:")
    if ope is '':
        ope = None
    else:
        ope = int(ope)
    #test nstyle:
    nStyles = [None,None,None,None,None,ope,None,None,None]
    vocaloid.change_note(note=note,y=y,p=p,t=t,dur=dur,n=n,v=v,nStyles=nStyles)


def interface_2(v,selected_part):
    print()
    begin=int(input("Enter the loc of 1st phonetic:"))
    choice='2'
    while choice != '0':
        print("Enter the Mode:")
        print("1. Every phonetic is ended with a '\\n'")
        print("2. Customize your splitting sign [DEFAULT]")
        print("0. Quit")
        choice=input("Your choice:")
        if choice == '':
            choice='2'
        if choice == '1':
            p=serialize_phonetic_with_enter()
        if choice == '2':
            p=serialize_phonetic_customize()
        if choice is '0':
            return
        v.incept_phonetic(selected_part,p,begin)
def serialize_phonetic_with_enter():
    print()
    print("Enter the phonetic, and end up your input with 0")
    p=[]
    while True:
        a=input()
        if a is '0':
            break
        p.append(a)
    return p
def serialize_phonetic_customize():
    print("\nEnter the sign you want to split the phonetic.")
    print("But attention: some sign will make this program be F**ked,")
    print("so choice the sign carefully.\nDO NOT USE '-'!!!")
    sign=input("Input it here:")
    p=input("Now you can input them in your way:\n").split(sign)
    return p
def interface_9(v,original_path):
    print("\nSave File:")
    choice=input("1 for original file and 2 for another file")
    if choice is '1':
        path=original_path
    elif choice is '2':
        path=input("File name(you needn't add '.vsqx' at the end of filename):")
        path+='.vsqx'
    else:
        print("Choice is invailed.")
        return
    dat=v.save_vsqx().decode()
    dat=endprocess(dat)
    with open(path,'w') as f:
        f.write(dat)
    print("Saved successfully.")
    return True
def mian():
    if debug:
        path="51.vsqx"
    else:
        path=input('Please input the path of original vsqx file')
    #deal with CDATA data
    dat=open(path).read()
    dat=preprocess(dat)
    #end deal with CDATA
    v=vsqx_option(data=dat,path=None)
    #part=v.start_doing()
    #v.append_note(element_path=part,location=2880,lrc='ra',phonetic='4 a')
    #v.incept_phonetic(part,["4 a","4 a"])
    dat=v.save_vsqx().decode()
    dat=endprocess(dat)
    with open('ldld3.vsqx','w') as f:
        f.write(dat)
    

if __name__ == "__main__":
    while True:
        input("========PRESS ANY KEY========")
        interface("test1.vsqx")
        #mian()
