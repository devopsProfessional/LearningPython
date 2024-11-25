''' This module creates a tree and shoe the traversal'''
class TreeNode: # pylint: disable=too-few-public-methods
    '''
    This class is to initialize a tree node and add child nodes
    '''
    def __init__(self, data):
        """
         Treenode class with traversal
        :param data:
        """
        self.data = data
        self.childnodes = []
    #### Function to add a child node in tree
    def add_childnode(self,node):
        '''
        This function will add the child node to the tree
        :param node:
        :return:
        '''
        self.childnodes.append(node)



def pre_order_traversal(node):
    '''
    Pre-Order Traversal Function (Recursion)
    '''
    if node is None:
        return
    print(node.data)
    for child in node.childnodes:
        pre_order_traversal(child)


def post_order_traversal(node):
    '''
    Post-Order Traversal Function (Recursion)
    '''
    if node is None:
        return
    for child in node.childnodes:
        post_order_traversal(child)
    print(node.data)


root = TreeNode("R")
node1 = TreeNode("A")
node2 = TreeNode("C")
node3 = TreeNode("D")

root.add_childnode(node1)
root.add_childnode(node2)
root.add_childnode(node3)

print ("Pre Order traversal of a tree")
pre_order_traversal(root)

print ("Post Order traversal of a tree")
post_order_traversal(root)
