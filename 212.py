#Function to count number of nodes in BST that lie in the given range.
def getCount(root,low,high):
    
    c = [0]
    
    def inOrder(root, c, low, high):
        
        if root==None:
            return 
        
        inOrder(root.left, c, low, high)
        
        if low <= root.data <= high:
            print("ans: ", root.data)
            c[0]+=1
        
        inOrder(root.right, c, low, high)
        
    inOrder(root, c, low, high)
    
    return c[0]
