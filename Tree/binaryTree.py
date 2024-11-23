class BTree:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None
        
""""
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
