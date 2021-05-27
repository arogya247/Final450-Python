## GFG 
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(height of tree)
 

def check(self, root):

        if root==None:
            return 

        # this list will keep all the nodes of the current level
        q_curr = []

        # this list will keep all the nodes of the next level
        q_next = []

        # store the root node in q_curr for starting
        q_curr.append(root)

        # use of count_i and count_f here is that count_i is the nmbr of nodes in the 
        # current level and count_f will increase after checking if the curr node has 
        # a child or not 
        count_i=1
        count_f=0

        while(len(q_curr)!=0):

            # temp is the first element of q_curr
            temp = q_curr[0]

            q_curr.pop(0)

            # if the node has child(left or right), increase count_f
            if temp.left or temp.right:
                count_f+=1


            if temp.left:
                q_next.append(temp.left)
            if temp.right:
                q_next.append(temp.right)

            # when the length of q_curr becomes zero, we will compare count_i and count_f, 
            # they will be same if every node of that level is same or not
            if len(q_curr)==0:
                if count_f!=count_i and count_f!=0:
                    return False
                q_curr,q_next = q_next, q_curr
                count_i = len(q_curr)
                count_f=0

        return True


