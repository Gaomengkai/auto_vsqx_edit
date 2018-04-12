from xml.dom.minidom import parse
from xml.dom.minidom import Document
import xml.dom.minidom


debug=True


class vsqx_option():
    def __init__(self,path):
        self.CurrentData=''
        self.notes=[]
        self.path=path
        self.phonetic=[]
        self.number=0
        self.lrc=[]
    
    def startDoing(self):
        self.DOMTree=xml.dom.minidom.parse(self.path)
        self.tree=self.DOMTree.documentElement
        self.notes=self.tree.getElementsByTagName('note')
        for note in self.notes:
            y1=note.getElementsByTagName('y')[0].firstChild.data
            p1=note.getElementsByTagName('p')[0].firstChild.data
            self.lrc.append(y1)
            self.phonetic.append(p1)

        if debug:
            print('[DEBUG] Notes:',len(self.notes))
            for i in range(0,len(self.lrc)):
                print('[DEBUG]      Lrc[',i,'] :',self.lrc[i])
                print('[DEBUG] Phonetic[',i,'] :',self.phonetic[i])

    def appendNote(self,location,length,tone,lrc,phonetic):
        treeBackup=self.tree
        self.tree=
        willAppend = self.tree.createElement('note')
        vsPart=self.tree.getElementsByTagName('vsPart')
        vsPart[0].appendChild(willAppend)
        notes=vsPart.getElementsByTagName('note')
        note=notes[len(notes)-1]
        t=self.tree.createElement('t')
        dur=self.tree.createElement('dur')
        n=self.tree.createElement('n')
        v=self.tree.createElement('v')
        y=self.tree.createElement('y')
        p=self.tree.createElement('p')
        nStyle=self.tree.createElement('nStyle')

        #int data:
        t.nodeType=dur.nodeType=n.nodeType=y.nodeType=3
        t.nodeValue=location
        dur.nodeValue=length
        n.nodeValue=tone
        v.nodeValue=64
        
        #CDATA data:
        p.nodeType=y.nodeType=4
        y.nodeValue=lrc
        p.nodeValue=phonetic

        #append child:
        for i in [t,dur,n,y,p,nStyle]:
            note.appendChild(i)
        #Process nStyle:
        accent=bendDep=bendLen=decay=fallPort=opening=risePort=vibLen=vibType=self.tree.createElement('v')
        styles=[accent,bendDep,bendLen,decay,fallPort,opening,risePort,vibLen,vibType]
        for i in styles:
            nStyle.appendChild(i)
            i.nodeType=3
        accent.setAttribute('id','accent')
        accent.nodeValue=80
        bendDep.setAttribute('id','bendDep')
        bendDep.nodeValue=8
        bendLen.setAttribute('id','bendLen')
        bendLen.nodeValue=0
        decay.setAttribute('id','decay')
        decay.nodeValue=70
        fallPort.setAttribute('id','fallPort')
        fallPort.nodeValue=0
        opening.setAttribute('id','opening')
        opening.nodeValue=127
        risePort.setAttribute('id','risePort')
        risePort.nodeValue=0
        vibLen.setAttribute('id','vibLen')
        vibLen.nodeValue=66
        vibType.setAttribute('id','vibType')
        vibType.nodeValue=1

        #Didn't finish
        pass

    def saveVsqx(self,path):
        with open('dom_write.xml','w',encoding='UTF-8') as fh:
            self.tree.writexml(fh,indent='',addindent='\t',newl='\n',encoding='UTF-8')
            print('写入xml OK!')

def mian():
    if not debug:
        path=input("Please input the vsqx file path:")
    else:
        path="E:\\V_HOME\\Lrc_test\\Untitled2 - 副本o.xml"
    vsq=vsqx_option(path)
    try:
        vsq.startDoing()
        vsq.appendNote(location=2880,length=960,tone=73,lrc='sa',phonetic='s a')
        vsq.saveVsqx(12)

    except Exception as e:
        print("[FAIL]")
        print(repr(e))
    a=input("Press any key to exit")

if __name__ == "__main__":
    mian()