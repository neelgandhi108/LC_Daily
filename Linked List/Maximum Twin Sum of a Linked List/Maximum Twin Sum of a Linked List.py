class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head , head
        # Go till middle part of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev , curr = None , slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Sum first half and reverse of second half
        res = 0
        first , second = head , prev
        while second:
            res = max(res, first.val + second.val)
            first , second = first.next , second.next
        return res