# GFG

def levelOrder(self,root ):
        ans = []
        queue = []
        
        if root == None:
            return ans
        
        queue.append(root)
        
        while( len(queue) > 0):
            ans.append(queue[0].data)
            Node = queue.pop(0)
            
            if Node.left:
                queue.append(Node.left)
            if Node.right:
                queue.append(Node.right)
                
        return ans
