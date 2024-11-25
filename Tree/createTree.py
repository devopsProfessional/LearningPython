'''
Create a tree node class
'''
class TreeNode: # pylint: disable=too-few-public-methods
    '''
    Create a tree node class
    '''
    def __init__(self, data):
        '''
        Create a tree node class
        '''
        self.data = data
        self.childnodes = []

    def add_childnode(self,node):
        '''
        Create child nodes to tree
        '''
        self.childnodes.append(node)
