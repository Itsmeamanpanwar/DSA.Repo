# Deleting a Node in Linked List
 
class Node: 
  def __init__(self,data): 
    self.data = data 
    self.next = None 

def traverseAndPrint(head): 
  currentNode = head 
  while currentNode: 
    print(currentNode.data , end = " -> ")
    currentNode = currentNode.next 
  print("Null") 

def deleteSpecificNode(head,NodeToDelete): 
  if head == NodeToDelete:
    return head.next 

  currentNode = head 
  while currentNode.next and currentNode.next != NodeToDelete: 
    currentNode = currentNode.next 

  if currentNode.next is None: 
    return head

  currentNode.next = currentNode.next.next

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

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)
