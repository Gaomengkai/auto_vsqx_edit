from xml.dom.minidom import parse
from xml.dom.minidom import Document
import xml.dom.minidom

path="E:\\V_HOME\\Lrc_test\\Untitled2 - 副本o.xml"
    
DOMTree=xml.dom.minidom.parse(path)
tree=DOMTree.documentElement
notes=tree.getElementsByTagName('note')
print('[DEBUG] Notes:',len(notes))
for note in notes:
    print('[DEBUG] They are:',note.childNodes[0].data,'\n')
lrc=tree.getElementsByTagName('y')
phonetic=tree.getElementsByTagName('p')
