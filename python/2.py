# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""

        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next

        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        n3 = str(int(n2) + int(n1))

        res = None
        while n3:
            temp = ListNode(n3[0], res)
            res = temp
            n3 = n3[1:len(n3)]
        
        return res