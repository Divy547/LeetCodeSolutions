# Last updated: 8/9/2025, 2:26:43 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        middlePointer = head
        endPointer = head
        while endPointer!=None and endPointer.next!=None:
            middlePointer = middlePointer.next
            endPointer = endPointer.next.next

        return middlePointer