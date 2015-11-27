import xml.dom.minidom
import ast

class CXmladapter:

	def __init__(self,strUrl,strItem):
		self.strUrl=strUrl
		self.strItem=strItem



	def read(self,nNum):
		xmlFile=xml.dom.minidom.parse(self.strUrl)
		xmlItem=xmlFile.getElementsByTagName(self.strItem)
		xmlNumItem=xmlItem[nNum]
		strList=xmlNumItem.firstChild.data
		listItem=ast.literal_eval(strList)
		return listItem

a=CXmladapter('map.xml','map')
print a.read(0)


