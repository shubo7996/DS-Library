class Node(object):

	def __init__(self,character):
		self.character=character
		self.leftNode=None
		self.rightNode=None
		self.middleNode=None

#trie has 26 children, not memory erffiecient
#Ternary Search Trees are memory effcient
class TernaryTree(object):
	
	def __init__(self):
		self.rootNode=None
	
	def putItem(self, key, value):
		self.rootNode= self._putItem(self.rootNode,key,value,0)
	
	def _putItem(self,node,key,value,index):
		c=key[index]

		if node==None:
			node=Node(c)

		if c<node.character:
			node.leftNode=self.putItem(node.leftNode,key,value,index)
		elif c>node.character:
			node.rightNode=self.putItem(node.rightNode,ket,value,index)
		elif index<len(key)-1:
			node.middleNode=self.putItem(node.middleNode,key,value,index+1)
		else:
			node.value=value

	def getItem(self,key):
		node=self._getItem(self,key)

		if node==None:
			return None

		return node

	def _getItem(self,node, key, index):
		
		if node==None:
			return None

		c=key[index]

		if c<node.character:
			self._getItem(node.leftChild,key,index)
		elif c>node.character:
			self._getItem(node.rightChild,key,index)
		elif index<len(key)-1:
			self._getItem(node.middleNode,key,index)
		else:
			return Node

def main():

	tree=TernaryTree()
	tree.putItem("Mayukh",200)
	tree.putItem("Suvankar",600)
	tree.putItem("Rishabh",500)
	tree.putItem("Kaustav",300)

if __name__ == '__main__':
 	main() 











		