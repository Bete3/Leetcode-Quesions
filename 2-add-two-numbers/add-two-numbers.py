# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        temp = l1
        ptr = l2
        carry = 0

        while temp or ptr or carry:
            x = temp.val if temp else 0
            y = ptr.val if ptr else 0
            s = x + y + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            if temp:
                temp = temp.next
            if ptr:
                ptr = ptr.next
            curr = curr.next
        return dummy.next