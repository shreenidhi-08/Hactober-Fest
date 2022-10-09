#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        while head:

            temp=dummy
            nextNode=head.next

            while (temp.next and temp.next.val<head.val):
                temp=temp.next
            head.next=temp.next
            temp.next=head
            head=nextNode
        return dummy.next


        

        
# @lc code=end

