class Node(object):
	def __init__(self,value):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None
		self.height=1

class AVLTree(object):
	def __init__(self):
		self.root=None

	def __repr__(self):
		if self.root is None:
			return ''
		content= '\n'
		cur_node=[self.root] #all nodes at current level
		cur_height=self.root.height #height of nodes at current level
		sep= ''*(2**(cur_height-1)) #variable sized seperator between elements
		while True:
			cur_height+=-1 #decrementing current height
			if len(cur_node)==0:
				break
			cur_row=''
			next_row=''
			next_nodes=[]

			if all(n is None for n in cur_node):
				break

			for n in cur_node:
				if n==None:
					cur_row+='   '+sep
					next_row+='	  '+sep
					next_nodes.extend([None,None])
					continue

				if n.value!=None:
					buf=' '*((5-len(str(n.value)))/2)
					cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
				else:
					cur_row+=' '*5+sep

				if n.left_child!=None:
					next_nodes.append(n.left_child)
					next_row+='  /'+sep
				else:
					next_row+='   '+sep
					next_nodes.append(None)

				if n.right_child!=None:
					next_nodes.append(n.right_child)
					next_row+='  /'+sep
				else:
					next_row+='   '+sep
					next_nodes.append(None)

			content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'/n')
			cur_nodes=next_nodes
			sep=''*(len(sep)/2) #cut seperator size in half
		return content

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
				self._inspect_insertion(cur_node.left_child)
			else:
				self._insert(value,cur_node.left_child)
		elif value > cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=Node(value)
				cur_node.right_child.parent=cur_node #set parent to the current right child
				self._inspect_insertion(cur_node.right_child)
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
			print '%s,h=%d'%(str(cur_node.value),cur_node.height)
			self._printTree(cur_node.right_child)

	#def makeList(self,cur_node):
	#	if cur_node is None:
	#		return []
	#	return self.makeList(cur_node.left_child) + [cur_node.value] + self.makeList(cur_node.right_child)

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
			return

		if node_parent!=None:
			node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))
			self._inspect_deletion(node_parent)


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

	#new func for AVL

	def _inspect_insertion(self,cur_node,path=[]):
		if cur_node.parent is None:
			return
		path=[cur_node]+path
		
		left_height=self.get_height(cur_node.parent.left_child)
		right_height=self.get_height(cur_node.parent.right_child)

		if abs(left_height-right_height)>1:
			path=[cur_node.parent]+path
			self._rebalance_node(path[0],path[1],path[2])
			return

		new_height=1+cur_node.height
		if new_height>cur_node.parent.height:
			cur_node.parent.height=new_height

		self._inspect_insertion(cur_node.parent,path)

	def _inspect_deletion(self,cur_node):
		pass

	def _rebalance_node(self,x,y,z):
		pass

	def _right_rotate(self,z):
		pass

	def _left_rotate(self,z):
		pass

	def get_height(self,cur_node):
		pass

	def taller_child(self,cur_node):
		pass


