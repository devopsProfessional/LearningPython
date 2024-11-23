class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childnodes = []
    
    def add_childnode(self,node):
        self.childnodes.append(node)