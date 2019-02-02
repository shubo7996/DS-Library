class Node(object):
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList(object):
	def __init__(self):
		self.head=None

	def isListEmpty():
		if self.head is None:
			return True
		else:
			return False

	@property
	def listLength(self):
		currentNode=self.head
		length=0
		while currentNode is not None:
			length+=1
			currentNode=currentNode.next
		return length

	def insertAtHead(self,nodeObj):
		temporaryNode=self.head
		self.head=nodeObj
		self.head.next=temporaryNode
		del temporaryNode

	def insertAt(self,nodeObj,position):
		if position<0 or position>self.listLength:
			print('Invalid!')
			return
		if position==0:
			self.insertAtHead(nodeObj)
			return
		currentNode= self.head
		currentPosition=0
		while True:
			if currentPosition==position:
				previousNode.next=nodeObj 
				nodeObj.next=currentNode 
				break
			previousNode=currentNode
			currentNode=currentNode.next
			currentPosition+=1
		

	def insertData(self,nodeObj):
		#print("----inserting into LinkedList----")
		if self.head is None:
			self.head=nodeObj
		else:
			lastnode=self.head
			while True:
				if lastnode.next is None:
					break
				lastnode=lastnode.next
			lastnode.next=nodeObj
		#print("__Done__")

	def deleteHead(self):
		if self.isListEmpty() is False:
			previousHead=self.head
			self.head=self.head.next
			previousHead=Node
		else:
			print("Linked List is empty!")

	def deleteAtEnd(self):
		if self.isListEmpty() is False:
			if self.head.next is None:
				self.deleteHead()
				return
		lastnode=self.head
		while lastnode.next is not None:
			previousNode=lastnode
			lastnode=lastnode.next
		previousNode.next=None

	def deleteAt(self,position):
		if position<0 or position>=self.listLength:
			print("Invalid position!")
			return


		if self.isListEmpty() is not False:
			if position==0:
				self.deleteHead()
				return
			currentNode= self.head
			currentPosition=0
			while True:
				if currentPosition==position:
					previousNode.next=currentNode.next 
					currentNode.next=None 
					break
				previousNode=currentNode
				currentNode=currentNode.next
				currentPosition+=1

	def printList(self):
		if self.head is None:
			print("List is empty")
			return
		currentNode=self.head
		while True:
			#print("I am inside the print func!")
			if currentNode is None:
				break
			print(currentNode.data)
			currentNode=currentNode.next

def main():
	firstNode_obj=Node(data='Jack')
	secondNode_obj=Node(data='Colt')
	thirdNode_obj=Node(data='Shelly')
	headNode_obj=Node(data='Jessie')
	secondhalfNode_obj=Node(data="Bull")
	linkedlist_obj=LinkedList()
	linkedlist_obj.insertData(firstNode_obj)
	linkedlist_obj.insertData(secondNode_obj)
	linkedlist_obj.insertData(thirdNode_obj)
	linkedlist_obj.insertAtHead(headNode_obj)
	linkedlist_obj.insertAt(secondhalfNode_obj,position=0)
	linkedlist_obj.deleteAt(position=2)
	linkedlist_obj.printList()


if __name__ == '__main__':
	main()
	

