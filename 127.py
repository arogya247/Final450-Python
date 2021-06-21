## GFG

## Space and Time complexity needs to be corrected

def reverse(self,head, k):
        
        if head==None:
            return None
        curr = head
        prev = None
        next = None
        count=0
        
        while(curr!=None and count<k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count+=1
            
        if next is not None:
            head.next = self.reverse(next,k)
            
        return prev
