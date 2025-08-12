# Last updated: 8/12/2025, 11:47:45 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.middle(head)
        rightList = mid.next
        mid.next = None

        leftSorted = self.sortList(head)
        rightSorted = self.sortList(rightList)

        return self.merge(leftSorted, rightSorted)

    def middle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Attach the remaining part (like extend in arrays)
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next