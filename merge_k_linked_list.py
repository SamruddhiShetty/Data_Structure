# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap=[]
        for i in lists:
            while i:
                heappush(heap, i.val)
                i=i.next
        result=node=ListNode(-1)
        for i in range(len(heap)):
            node.next=ListNode(heappop(heap))
            node=node.next
        return result.next
                
        
        
