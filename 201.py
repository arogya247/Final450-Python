#Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        '''    
        # Traverse the tree in inorder fashion 
        # and keep track of previous node
        # return true if tree is Binary 
        # search tree otherwise false
        def isbst_rec(root):
            
            global prev
            
            # if tree is empty return True
            if root is None:
                return True
            
                
            if isbst_rec(root.left) is False:
                return False
                
            if prev!=None and prev.data >= root.data:
                return False
                
            prev = root
            return isbst_rec(root.right)
        
        
        global prev
        prev = None
        
        return isbst_rec(root)
        ''' 
        
        
        ## This is a great solution
        ## see gfg vid on u tube for explanation
        
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        
        def isBSTUtil(node, mini, maxi):
            
            # an empty tree is a bst
            if node is None:
                return True
                
            if node.data <= mini or node.data >= maxi:
                return False
                
            return (isBSTUtil(node.left, mini, node.data) and 
            isBSTUtil(node.right, node.data, maxi))
        
        
        return isBSTUtil(root, INT_MIN, INT_MAX)
        
        
        
        '''
        ## This soluton is discarded because it will not work for this case
        
                                    3
                                   / \
                                  2   5
                                 / \
                                1   4
                                
                
        if root == None:
            return True
        
        if root.left and self.isBST(root.left)==False:
            return False
        if root.right and self.isBST(root.right)==False:
            return False
            
            
        if ((root.left==None or root.left.data < root.data) and 
        (root.right==None or root.right.data > root.data)):
            return True
        else:
            return False
            
        '''
