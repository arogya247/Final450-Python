## GFG
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
        
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
