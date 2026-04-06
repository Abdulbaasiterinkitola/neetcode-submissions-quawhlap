# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr, fast_ptr = head, head

        while fast_ptr and fast_ptr.next: #to avoid trying to get next.next or next.next.next which do not exist. this covers for slow_ptr automatically too.
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True

        return False
        
        """not the best, but to follow as the question is
        slow_ptr, fast_ptr = head, head
        index = 0 #index is not really needed... just to follow the question till the end

        while fast_ptr and fast_ptr.next: #to avoid trying to get next.next or next.next.next which do not exist. this covers for slow_ptr automatically too.
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            index += 1

            if slow_ptr == fast_ptr:
                index = -1
                break #will enter infinite loop w/o this, and give TLE

        return not bool(index+1)
        """
            