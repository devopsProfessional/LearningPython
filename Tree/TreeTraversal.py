class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childnodes = []
    #### Function to add a child node in tree
    def add_childnode(self,node):
        self.childnodes.append(node)

"""
### Pre-Order Traversal Function (Recursion)
"""
def pre_order_traversal(node):
    if node is None:
        return  
    print(node.data)
    for child in node.childnodes:
        pre_order_traversal(child)

"""
### Post-Order Traversal Function
"""
def post_order_traversal(node):
    if node is None:
        return
    for child in node.childnodes:
        post_order_traversal(child)
    print(node.data)
          
          
          
"""          
##### Creating root nodes and child nodes
"""
root = TreeNode("R")
node1 = TreeNode("A")
node2 = TreeNode("C")
node3 = TreeNode("D")

"""
####### adding child nodes to the root 
"""
root.add_childnode(node1)
root.add_childnode(node2)
root.add_childnode(node3)

"""
#### Call Pre Order Traversal
"""
print ("Pre Order traversal of a tree")
pre_order_traversal(root)

"""
#### Call Post Order Traversal
"""
print ("Post Order traversal of a tree")
post_order_traversal(root)   
