## GFG
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

def addOne(self,head):
        
        ## Iterating till the last node so that we can find last non-9 number
        curr = head
        last = None
        while(curr):
            if curr.data != 9:
                last = curr
            curr = curr.next
                
        # If list is of the type 9 -> 9 -> 9 ...
        if last == None:
            #print("second case: ", last.data)
            temp = Node(1)
            temp.next = head
            while(head):
                head.data = 0
                head = head.next
            return temp
        
        # If list is of the type 2 -> 4 -> 7 -> 6
        elif last.next==None:
            #print("first case: ", last.data)
            last.data+=1
            return head
            
        # If list is of the type 2 -> 4 -> 9 -> 9 -> 9 -> 9.....
        else:
            #print("third case: ", last.data)
            last.data+=1
            last = last.next
            while(last!=None):
                last.data = 0
                last = last.next
                
            return head
