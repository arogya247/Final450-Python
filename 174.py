# GFG
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

def zigZagTraversal(root):
    if root == None:
        return

    flag=True
    
    ans = []
    q_curr = []
    q_next = []
    
    q_curr.append(root)
    
    while(len(q_curr)!=0):
        
        temp = q_curr[-1]
        q_curr.pop(-1)
        
        ans.append(temp.data)
        
        if flag==True:
            
            if temp.left!=None:
                q_next.append(temp.left)
            
            if temp.right!=None:
                q_next.append(temp.right)
        else:
            
            if temp.right!=None:
                q_next.append(temp.right)
            
            if temp.left!=None:
                q_next.append(temp.left)
            
            
        if len(q_curr)==0:
            flag = not(flag)
            q_curr, q_next = q_next, q_curr
            
    return ans
