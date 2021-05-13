def check(self, root):
        
        if root==None:
            return 
        
        q_curr = []
        
        q_next = []
        q_curr.append(root)
        count_i=1
        count_f=0
        while(len(q_curr)!=0):
            temp = q_curr[0]
            
            q_curr.pop(0)
            
            if temp.left or temp.right:
                count_f+=1
            
            if temp.left:
                q_next.append(temp.left)
            if temp.right:
                q_next.append(temp.right)
                
            if len(q_curr)==0:
                if count_f!=count_i and count_f!=0:
                    return False
                q_curr,q_next = q_next, q_curr
                count_i = len(q_curr)
                count_f=0
                
        return True    
