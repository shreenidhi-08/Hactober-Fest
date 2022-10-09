#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)

        prev=dummy
        curr=head
        for _ in range(left-1):
            prev=prev.next
            curr=curr.next

        leftSideHead=prev
        leftHead=curr

        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        leftSideHead.next=prev
        leftHead.next=curr

        return dummy.next


        
# @lc code=end

