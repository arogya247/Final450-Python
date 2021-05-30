# #GFG
# Expected Time Complexity: O(H +K)
# Expected Auxiliary Space: O(H)


def kthLargest(self, root, k):
        c = [0]    
        
        def check(root, c, k):
            
            if root==None or c[0] >= k:
                return 
            
            check(root.right, c, k)
            
            c[0]+=1
            if c[0]==k:
                #print("ans-->  ",root.data)
                return root.data
            # print("count--> ", c[0])
            # print("root==>", root.data)
                
            check(root.left, c, k)
        
        
        return check(root, c, k)
