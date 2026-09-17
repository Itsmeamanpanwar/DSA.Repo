# Insert a Node 

class Node: 
  def __init__(self,data): 
    self.data = data 
    self.next = None 

def TraverseAndPrint(head): 
  currentNode = head
  while currentNode:
    print(currentNode.data, end = " -> ") 
    currentNode = currentNode.next 

  print("Null") 

def InsertNodeAtPosition(head,newNode,Position): 
  if Position == 1: 
    newNode.next = head 
    return newNode

  currentNode = head
  for _ in range(Position - 2): 
    if currentNode.next is None: 
      break 
    currentNode = currentNode.next

  newNode.next = currentNode.next 
  currentNode.next = newNode 
  return head


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(9)
node5 = Node(8)
node6 = Node(5)
node7 = Node(2) 

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print("Original List: ")
TraverseAndPrint(node1) 

# Inserting a new node with value 97 at position 2
NewNode = Node(97) 
node1 = InsertNodeAtPosition(node1, NewNode , 2)

print("After Insertion: ")
TraverseAndPrint(node1)