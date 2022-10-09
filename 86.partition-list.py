#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

		#Creating DummyNode for Node smaller and (equal or larger) than x. 
        smallerList=ListNode(0)
        largerList=ListNode(0)

		#Saving pointer of Smaller and larger partition
        smallerHead=smallerList
        largerHead=largerList
        
        # Iterate through all Node
        while head:
            if head.val<x:
                #If val of current Node is Smaller than X Link that Node to smaller partition
                smallerList.next=head
                smallerList=smallerList.next
                
            else:
                # else val of current Node is equal or larger than X Link that Node to larger partition
                largerList.next=head
                largerList=largerList.next
        
            # Move head ptr to next Node
            head=head.next

		# Link smaller Partition Last Node to Larger Partition Head Node
        smallerList.next=largerHead.next
		#Larger partition Last Node to None
        largerList.next=None

        #Return Smaller partition starting Node
        return smallerHead.next      
# @lc code=end

