# GFG
# Expected Time Complexity: O(NLogN)
# Expected Auxiliary Space: O(N)   
  
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        # code here
        
        def inorder(root, arr):
            
            if root==None:
                return 
            
            inorder(root.left, arr)
            
            arr.append(root.data)
            
            inorder(root.right, arr)
            
            return arr
            
        def insertOrder(root, arr):
            
            if root==None:
                return 
            
            insertOrder(root.left, arr)
            
            root.data = arr.pop(0)
            
            insertOrder(root.right, arr)
            
            return root
            
        ## tarversing in inorder we will store all the 
        ## elements of the tree in an array    
        arr1 = inorder(root,[])
        
        ## bcoz inorder traversal of a **TRUE BST** gives sorted array
        ## we will sort the array b4 moving ahead
        arr1.sort()
        
        ## once we have the array sorted we just have to traverse the tree in inorder
        ## and replace values in the nodes of binary tree with the values in 
        ## the array without changing the structure of the tree
        return insertOrder(root,arr1)
