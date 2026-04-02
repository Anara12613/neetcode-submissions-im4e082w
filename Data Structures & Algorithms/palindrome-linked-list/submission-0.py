# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle(head):
            slow = head
            fast = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(head):
            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        mid = middle(head)
        sec = reverse(mid)
        first = head

        while first and sec:
            if first.val != sec.val:
                return False
            first = first.next
            sec = sec.next
        
        return True



        
        