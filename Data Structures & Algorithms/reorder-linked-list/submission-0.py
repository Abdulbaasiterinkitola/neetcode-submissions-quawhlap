# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s_ptr, f_ptr = head, head.next

        #divide into 2 halves
        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next
            s_ptr = s_ptr.next

        half2 = s_ptr.next
        s_ptr.next = None
        prev = s_ptr.next

        #reverse 2nd half
        while half2:
            nxt = half2.next
            half2.next = prev
            prev = half2
            half2 = nxt

        #merge
        half1, half2 = head, prev
        while half2:
            tmp1, tmp2 = half1.next, half2.next
            half1.next = half2
            half2.next = tmp1
            half1, half2 = tmp1, tmp2
            

        



