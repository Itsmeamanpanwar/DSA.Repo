class TreeNode: 
  def __init__(self,data): 
    self.data = data 
    self.right = None
    self.left = None 

root = TreeNode('R') 
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeH = TreeNode('H') 

root.left = nodeA
nodeA.right = nodeB 

nodeB.left = nodeC 
nodeC.right = nodeD 

nodeD.left = nodeE
nodeE.right = nodeF 

nodeF.left = nodeG 
nodeG.right = nodeH

def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")

postOrderTraversal(root)