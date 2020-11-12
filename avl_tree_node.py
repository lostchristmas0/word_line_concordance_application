from tree_node import TreeNode

class AVLTreeNode(TreeNode):
    def __init__(self,key,val,left=None,right=None,
                 parent=None, balanceFactor=0):
        TreeNode.__init__(self,key,val,left,right,parent)
        self.balanceFactor = balanceFactor
