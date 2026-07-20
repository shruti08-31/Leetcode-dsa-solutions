class Solution:
    def addTwoNumbers(self, l1, l2):
        d= ListNode(0)
        curr= d
        carry= 0
        while l1 or l2 or carry:
            if l1:
                val1= l1.val
            else:
                val1= 0

            if l2:
                val2= l2.val
            else:
                val2= 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1= l1.next

            if l2:
                l2= l2.next
        return d.next