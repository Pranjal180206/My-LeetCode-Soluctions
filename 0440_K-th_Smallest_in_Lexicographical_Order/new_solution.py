# Problem: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Method: Lexicographical Tree

class Solution(object):
    def findKthNumber(self, n, k):
        def count_prefix(curr, n):
            count = 0
            next_curr = curr + 1
            while curr <= n:
                count += min(n + 1, next_curr) - curr
                curr *= 10
                next_curr *= 10
            return count
        curr = 1
        k -= 1
        while k > 0:
            steps = count_prefix(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr
