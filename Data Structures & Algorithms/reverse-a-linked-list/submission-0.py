# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #to create an extra empty bucket-like scenario
        curr = head # start with the first value

        while curr:
            next_val = curr.next # step 3 needed to get this value not manipulated already by step 1 before being used in step 4
            curr.next = prev # step 1 to flip the arrow (i.e the link in the linkedlist)
            prev = curr # step 2 to move prev one step further into the linkedlist
            curr = next_val # step 4 to continue the reversal for the next value. won't return error for the last value since the linkedlist already handles that by setting the last value . next to None

        return prev #this results in None <- 1 <- 2 <- 3 <- 4 for an original linkedlist of 1 -> 2 -> 3 -> 4 -> None