#GFG
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(Height of the Tree).


def LeftView(root):
    ans = []
    q = []
    
    if root==None:
        return ans
        
    q.append(root)
    while(len(q)!=0):
        
        n = len(q)
        
        for i in range(1,n+1):
            temp = q[0]
            q.pop(0)
            
            if i==1:
                ans.append(temp.data)
                
            if temp.left:
                q.append(temp.left)
                
            if temp.right:
                q.append(temp.right)
                
    return ans
