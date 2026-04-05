# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res #both tail and res initially point to the same address, and because objects (unlike integers) are mutable, any change to tail.next also modifies the object res points to. We return res.next (not tail.next) because res remains a fixed reference to the start of the list, while tail has moved to the very end during the merge
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if list1:
            tail.next = list1

        else:
            tail.next = list2

        return res.next #why return res.next rather than tail.next
        
        """
        #this code is wrong for returning a list rather than a listnode. Even if it should return a list, it can be simplified
        res = []

        head1, head2 = list1, list2

        while head1 or head2:
            if head1 and head2:
                if head1.val == head2.val:
                    res.append(head1.val)
                    res.append(head2.val)
                    head1 = head1.next
                    head2 = head2.next

                elif head1.val < head2.val:
                    res.append(head1.val)
                    head1 = head1.next

                elif head2.val < head1.val:
                    res.append(head2.val)
                    head2 = head2.next

            elif head1:
                res.append(head1.val)
                head1 = head1.next

            elif head2:
                res.append(head2.val)
                head2 = head2.next
                
        
        return res"""
