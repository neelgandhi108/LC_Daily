class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr , curr = [] , head
        while curr:
            arr.append(curr)
            curr = curr.next
        n = len(arr)
        base_len , remainder  = n // k , n % k
        start = 0
        res = [None] * k
        for i in range(k):
            if start < n:
                res[i] = arr[start]
                tail = start + base_len - 1
                if remainder:
                    tail += 1
                    remainder -= 1
                arr[tail].next = None
                start = tail + 1
        return res