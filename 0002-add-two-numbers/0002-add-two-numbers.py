class Solution:
    def addTwoNumbers(self, l1, l2):
        t = l1
        s = l2
        a = []
        b = []

        while t:
            a.append(t.val)
            t = t.next

        while s:
            b.append(s.val)
            s = s.next

        n = max(len(a), len(b))
        arr = []
        carry = 0

        for i in range(n):
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0

            total = x + y + carry
            arr.append(total % 10)
            carry = total // 10

        if carry:
            arr.append(carry)

        head = ListNode(arr[0])
        curr = head

        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next

        return head