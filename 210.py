## GFG


## we will use iterative inorder traversal of a bst in this problem
## also we will traverse 2 trees at the same time, one inorder and other reverse inorder
def countPairs(root1, root2, x):
    
    
    if root1==None or root2==None:
        return None
        
    #initialize 2 stacks for both trees respectively    
    st1 = []
    st2 = []
    
    # count of pairs with sum equal to x
    count=0
    
    # loop will run until one of both the stacks get empty
    while(True):
        
        ## this is basic iterative inorder traversal of a bst used here
        while(root1!=None):
            st1.append(root1)
            root1 = root1.left
            
        while(root2!=None):
            st2.append(root2)
            root2 = root2.right
            
        if len(st1)==0 or len(st2)==0:
            break
        
        top1 = st1[len(st1)-1]
        top2 = st2[len(st2)-1]
        
        if (top1.data + top2.data) == x:
            count+=1
            
            st1.pop()
            st2.pop()
            
            root1 = top1.right
            root2 = top2.left
            
        elif (top1.data + top2.data) > x:
            st2.pop()
            root2 = top2.left
        else:
            st1.pop()
            root1 = top1.right
        
    return count    
