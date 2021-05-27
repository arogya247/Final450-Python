# Leetcode
# Time Complexity: O(height of tree)

def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # Base Case
        if root == None:
            return root  
        
        #if key to be deleted is smaller than root the it lies to the left
        #if key to be deleted is greater than root the it lies to its right
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        else:
            
            if root.left is None and root.right is None:
                return None
                
            elif root.left is None:
                return root.right
                
            elif root.right is None:
                return root.left
            
            # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            else:
                temp = root.right
                while(temp.left):
                    temp = temp.left
                    
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
                
        return root
