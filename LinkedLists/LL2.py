# Finding lowest Value in list 
class Node: 
  def __init__(self,data): 
    self.data = data 
    self.next = None 

def FindLowestValue(head): 
  minValue = head.data
  currentNode = head.next 
  while currentNode: 
    if currentNode.data < minValue: 
      minValue = currentNode.data 
    currentNode = currentNode.next
  return minValue 

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

print(f"Lowest Value in the Linked List is : {FindLowestValue(node1)}")

