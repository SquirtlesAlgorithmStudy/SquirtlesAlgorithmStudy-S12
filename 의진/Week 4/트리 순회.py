import sys
input = sys.stdin.readline

class Node:  
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.data)
class Tree:
  def __init__(self):
    self.root = None

  def preorderTraversal(self, node):
    print(node, end="")
    if not node.left == None: self.preorderTraversal(node.left)
    if not node.right == None: self.preorderTraversal(node.right)

  def inorderTraversal(self, node):
    if not node.left == None: self.inorderTraversal(node.left)    
    print(node, end="")
    if not node.right == None: self.inorderTraversal(node.right)

  def postorderTraversal(self, node):
    if not node.left == None: self.postorderTraversal(node.left)   
    if not node.right == None: self.postorderTraversal(node.right) 
    print(node, end="")  
  def makeRoot(self, node):
    if self.root == None:
     self.root = node



    
n = int(input())
nodedatas = []
nodes = []
for _ in range(n):
  data = list(input().split())
  nodedatas.append(data)
for i in range(n):
  node = Node(nodedatas[i][0])
  nodes.append(node)
for i in range(n):
  if nodedatas[i][1] != '.':
    for j in range(n):
      if nodedatas[i][1] == nodedatas[j][0]: 
       nodes[i].left = nodes[j]
       break
for i in range(n):
  if nodedatas[i][2] != '.':
    for j in range(n):
      if nodedatas[i][2] == nodedatas[j][0]: 
       nodes[i].right = nodes[j]
       break

 
tree = Tree()
tree.makeRoot(nodes[0])



tree.preorderTraversal(tree.root)
print("")
tree.inorderTraversal(tree.root)
print("")
tree.postorderTraversal(tree.root)





