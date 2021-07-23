## Bottom view of a binary tree
## GFG 

class Solution:
    def bottomView(self, root):
        # code here
        ans = []
        if root==None:
            return 
        
        hd = 0
        m = dict()
        q = []
        root.hd = hd
        
        q.append(root)
        
        while(len(q)!=0):
            temp = q[0]
            q.pop(0)
            
            hd = temp.hd
            
            m[hd] = temp.data
            
            if temp.left:
                temp.left.hd = hd-1
                q.append(temp.left)
            
            if temp.right:
                temp.right.hd = hd+1
                q.append(temp.right)
        
        for i in sorted(m):
            ans.append(m[i])
        #print(m)
        return ans
