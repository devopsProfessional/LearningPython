class BTree:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None
        
"""
###### Function to traverse in pre order
"""
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    
"""
###### Function to traverse  in-order
"""
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

""" 
###### Function to traverse post order
"""
def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)

"""
##### Create nodes ####
"""
root  = BTree("R")
node1 = BTree("A")
node2 = BTree("B")
node3 = BTree("C")
node4 = BTree("D")
node5 = BTree("E")
node6 = BTree("G")

"""
#### Create Binary tree by attaching the nodes
"""
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

""""
##### Traverse the tree
"""
print("Traverse pre order")
pre_order_traversal(root)

print ("Traverse in-order")
in_order_traversal(root)

print("Post-order traversal")
post_order_traversal(root)
