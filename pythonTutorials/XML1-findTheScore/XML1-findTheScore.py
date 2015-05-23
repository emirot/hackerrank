__author__ = 'nolanemirot'
import xml.etree.ElementTree as etree



if __name__ == '__main__':
    xml = ""
    nbAttrib = 0
    nbTests =  int(input())
    for i in range(0, nbTests):
        xml += input()
    tree = etree.ElementTree(etree.fromstring(xml))
    # for elem in tree.getroot():
    #     #print(elem.attrib)
    #     nbAttrib += len(elem.attrib)
    #     print("elem",elem.length)
    #     for el in elem:
    #         print(el)
    for elem in tree.iter():
        nbAttrib += len(elem.attrib)
    print(nbAttrib)