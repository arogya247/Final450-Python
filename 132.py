## GFG

#Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        
        curr = head
        map1 = set()
        map1.add(curr.data)
        while(curr.next):
            if curr.next.data in map1:
                curr.next = curr.next.next
            else:
                map1.add(curr.next.data)
                curr = curr.next
                
        return head
