## GFG
# Expected Time Complexity : O(n+m)
# Expected Auxilliary Space : O(n+m)
# Note: n,m are the size of the linked lists.


def findIntersection(head1,head2):
    
    head3 = Node(None)
    
    while(head1 and head2):
        if head1.data == head2.data:
            if head3.data == None:
                head3 = Node(head1.data)
                last = head3
            else:
                last.next = Node(head1.data)
                last = last.next
            
            head1 = head1.next
            head2 = head2.next
            
        elif head1.data < head2.data:
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
            
            
    return head3
