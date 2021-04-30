# GFG
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(Height of the Tree).


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        
        if root==None:
            return 
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
