## GFG
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


def detectLoop(self, head):
        slow = head
        fast = head
        
        while(slow!=None and fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                return True
                
        return False
