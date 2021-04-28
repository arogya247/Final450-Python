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
    
    def height(node):
        
        if node == None:
            return 0
        else:
            lheight = height(node.left)
            rheight = height(node.right)
        
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
            
            
    def printGivenLevel(root,level):
        
        if root is None:
            return 
        if level==1:
            ans.append(root.data)
        elif level>1:
            printGivenLevel(root.left,level-1)
            printGivenLevel(root.right,level-1)
    
    
    h = height(root)
    for i in range(h+1,0,-1):
        printGivenLevel(root,i)
        
    return ans
