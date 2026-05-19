# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        min_heap = []
        for i in range (len(lists)):
            if lists[i]:
                heapq.heappush(min_heap,(lists[i].val,i))
        while min_heap:
            val,i = heapq.heappop(min_heap)
            curr.next = lists[i]
            curr = curr.next

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap,(lists[i].val,i))
        return dummy.next





        