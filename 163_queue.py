## GFG
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    ans = []
    queue = []
    
    if root == None:
        return ans
        
    queue.append(root)
    
    while(len(queue) > 0):
        
        ans.append(queue[0].data)
        Node = queue.pop(0)
        
        if Node.right:
            queue.append(Node.right)
        if Node.left:
            queue.append(Node.left)
            
    return ans[::-1]
