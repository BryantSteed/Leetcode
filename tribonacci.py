class Solution:
    def tribonacci(self, n: int) -> int:
        """Leetcode 1137. N-th Tribonacci Number"""
        if not hasattr(self, "memo"):
            self.memo = [0, 1, 1]
        if n < len(self.memo):
            return self.memo[n]
        ans = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        self.memo.append(ans)
        return ans