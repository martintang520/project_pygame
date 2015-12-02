import xml.dom.minidom
import ast


# read the XML file and return a list
class CXmladapter:

	#Read the XML file
	def __init__(self,strUrl,strItem):
		self.strUrl = strUrl
		self.strItem = strItem

	# Return a specific list
	def Read(self,nNum):
		xmlFile = xml.dom.minidom.parse(self.strUrl)
		xmlItem = xmlFile.getElementsByTagName(self.strItem)
		xmlNumItem = xmlItem[nNum]
		strList = xmlNumItem.firstChild.data
		listItem =ast.literal_eval(strList)
		return listItem


