#Function to find the minimum element in the given BST.
def minValue(root):
    
    if root==None:
        return None
        
    while(root.left):
        
        root = root.left
        
        
    return root.data
