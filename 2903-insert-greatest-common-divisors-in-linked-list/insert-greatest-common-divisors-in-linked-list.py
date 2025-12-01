# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        curr = head
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            new_node = ListNode(g, curr.next)
            curr.next = new_node
            curr = new_node.next   

        return head
