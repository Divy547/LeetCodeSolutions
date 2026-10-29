# Last updated: 10/29/2026, 9:36:34 PM
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