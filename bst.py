class Node(object):
	def __init__(self,value):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None

class BST(object):
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			self.root=Node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value < cur_node.value:
			if cur_node.left_child==None:
				cur_node.left_child=Node(value)
				cur_node.left_child.parent=cur_node #set parent to the current left child
			else:
				self._insert(value,cur_node.left_child)
		elif value > cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=Node(value)
				cur_node.right_child.parent=cur_node #set parent to the current right child
			else:
				self._insert(value,cur_node.right_child)
		else:
			print("Value Already Exists!")
			#self._insert(value,cur_node.right_child)		

	@property
	def printTree(self):
		if self.root!=None:
			self._printTree(self.root)

	def _printTree(self,cur_node):
		if cur_node!=None:
			self._printTree(cur_node.left_child)
			print(str(cur_node.value))
			self._printTree(cur_node.right_child)

	def makeList(self,cur_node):
		if cur_node is None:
			return []
		return self.makeList(cur_node.left_child) + [cur_node.value] + self.makeList(cur_node.right_child)

	def search(self,value):
		if self.root==None:
			return False
		else:
			return self._search(value,self.root)

	def _search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.left_child!=None:
			 self._search(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			 self._search(value,cur_node.right_child)
		return False

	def find(self,value):
		if self.root!=None:
			return self._find(value,self.root)
		else:
			return None

	def _find(self,value,cur_node):
		if value==cur_node.value:
			return cur_node
		elif value<cur_node.value and cur_node.left_child!=None:
			self._find(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			self._find(value,cur_node.right_child)

	def delete_value(self,value):
		return self.delete_node(self.find(value))

	def delete_node(self,node):
		
		#returns the node with min value rooted at input node
		def min_value_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		#return number of children for specified node
		def number_of_child(n):
			numberOfChild=0
			if n.left_child!=None:
				numberOfChild+=1
			if n.right_child!=None:
				numberOfChild+=1
			return numberOfChild

	
		node_parent= node.parent
		
		node_children=number_of_child(node)

		#case 1 (if node has no children)
		if node_children==0:
			#remove reference from parent node
			if node_parent.left_child==node:
				node_parent.left_child=None
			else:
				node_parent.right_child=None

		#case 2 (if node has a single child)
		if node_children==1:

			#get the child node
			if node.left_child!=None:
				child=node.left_child
			else:
				child=node.right_child

			#replace the node to be deleted with the child node
			if node_parent.left_child==node:
				node_parent.left_child=child
			else:
				node_parent.right_child=child
			#correct the parent pointer
			child.parent=node_parent


		#case 3
		if node_children==2:

			successor=min_value_node(node.right_child)
			node.value=successor.value
			self.delete_node(successor)


	def height(self):
		if self.root==None:
			return 0
		else:
			return self._height(self.root,0)

	def _height(self,cur_node,cur_height):
		if cur_node==None:
			return cur_height
		left_child_height=self._height(cur_node.left_child,cur_height+1)
		right_child_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_child_height,right_child_height)

list2=[]
def generateNumber(tree,num_elems=10,maxInt=50):
	from random import randint
	for _ in range(num_elems):
		currentelement= randint(1,maxInt)
		list2.append(currentelement)
		tree.insert(currentelement)
	print("unsorted list:", list2)
	return tree


def main():
	tree=BST()
	tree.insert(5)
	tree.insert(10)
	tree.insert(13)
	tree.insert(2)
	tree.insert(1)
	tree.insert(3)
	tree.insert(23)
	#fill_tree=generateNumber(tree=tree)
	sorted=tree.makeList(tree.root)
	print("sorted list:", sorted)
	print(tree.search(8))
	print("Height of the Tree is", tree.height())
	tree.delete_value(23)
	tree.printTree

if __name__ == '__main__':
	main()
