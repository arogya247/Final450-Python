## GFG

def removeLoop(self, head):
        
        slow = fast = head
        
        while(slow and fast and fast.next):
            slow = slow.next 
            fast = fast.next.next
            
            if slow==fast:
                if fast==head:
                    while(fast.next!=slow):
                        fast = fast.next
                    fast.next=None
                    return head
                else:
                    slow = head
            
                    while(slow.next != fast.next):
                        slow = slow.next
                        fast = fast.next
                        
                    fast.next=None
                    return head
                
        return False
