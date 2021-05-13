# GFG
# Expected time complexity: O(N)
# Expected auxiliary space: O(h) , where h = height of tree

#Function to check whether a binary tree is balanced or not.
def isBalanced(root):
    
    if root == None:
        return True
    
    def height(node):
        
        if node == None:
            return False
            
        left = height(node.left)
        right = height(node.right)
        
        return max(left+1,right+1)
        
    lh = height(root.left)
    rh = height(root.right)
        
    if (abs(lh-rh)<=1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True
    
    return False
