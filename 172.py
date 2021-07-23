class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        ans = []
        if root==None:
            return 
        
        m = dict()
        q = []
        q.append(root)
        hd = 0
        root.hd = hd
        
        while(len(q)!=0):
            temp = q[0]
            q.pop(0)
            
            hd = temp.hd
            
            if hd not in m:
                m[hd] = temp.data
                
            if temp.left:
                temp.left.hd = hd-1
                q.append(temp.left)
            
            if temp.right:
                temp.right.hd = hd+1
                q.append(temp.right)
                
                
        for i in sorted(m):
            ans.append(m[i])
            
        return ans
