# GFG
# Expected Time Complexity: O(Height of the BST)
# Expected Auxiliary Space: O(Height of the BST)


#Function to find the lowest common ancestor in a BST. 
def LCA(root, n1, n2):
    
    ## if both the nodes are less than root, the LCA will be on the left side 
    if root.data > n1 and root.data > n2:
        return LCA(root.left, n1, n2)
        
    ## if both the nodes are greater than root, the LCA will be on the right side 
    elif root.data < n1 and root.data < n2:
        return LCA(root.right, n1, n2)
    
    ## if both the cases are not true, root will be your LCA
    else:
        return root
