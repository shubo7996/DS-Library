class Node(object):

	def __init__(self,character,value):
		self.character=character
		self.leftNode=None
		self.rightNode=None
		self.middleNode=None

#trie has 26 children, not memory erffiecient
#Ternary Search Trees are memory effcient
class TernaryTree(object):
	
	def __init__(self):
		self.rootNode=None
	
	def putItem(self,key, value):
		self.rootNode= self._putItem(self.rootNode,key,value,0)
	
	def _putItem(self,node,key,value,index):
		c=key[index]

		if node==None:
			node=Node(c)

		if c<node.character:
			node.leftNode=self._putItem(node.leftNode,key,value,index)
		elif c>node.character:
			node.rightNode=self._putItem(node.rightNode,key,value,index)
		elif index<len(key)-1:
			node.middleNode=self._putItem(node.middleNode,key,value,index+1)
		else:
			node.value=value
			#print(node.value)

		return node

	def getItem(self,key):
		node=self._getItem(self.rootNode,key,0)

		if node==None:
			return None

		print(node.value)
		return node.value

	def _getItem(self,node,key, index):
		
		if node==None:
			return None

		c=key[index]

		if c<node.character:
			return self._getItem(node.leftNode,key,index)
		elif c>node.character:
			return self._getItem(node.rightNode,key,index)
		elif index<len(key)-1:
			return self._getItem(node.middleNode,key,index)
		else:
			return node

def main():

	tree=TernaryTree()
	
	tree.putItem("Mayukh",200)
	tree.putItem("Suvankar",600)
	tree.putItem("Rishabh",500)
	tree.putItem("Kaustav",300)

	print(tree.getItem("Rishabh"))
	print(tree.getItem("Suvankar"))

if __name__ == '__main__':
 	main() 











		