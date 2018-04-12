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
        if debug:
            print('[DEBUG] Notes:',len(self.notes))
            for i in self.notes:
                print('[DEBUG] They are:',i.childNodes[0].data,'\n')
        self.lrc=self.tree.getElementsByTagName('y')
        self.phonetic=self.tree.getElementsByTagName('p')
        

def mian():
    if not debug:
        path=input("Please input the vsqx file path:")
    else:
        path="E:\\V_HOME\\Lrc_test\\Untitled2 - 副本o.xml"
    vsq=vsqx_option(path)
    try:
        vsq.startDoing()
    except Exception as e:
        print("[FAIL]")
        print(repr(e))
    a=input("Press any key to exit")



if __name__ == "__main__":
    mian()
