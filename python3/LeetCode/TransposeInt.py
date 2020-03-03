class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        over = (1 << 31) - 1 if x > 0 else (1 << 31)
        while y > 0:
            res = res * 10 + y % 10
            y //= 10
            if res > over:
                return 0
        return res if x > 0 else -res


s = Solution()
print(s.reverse(x=123))
print(s.reverse(x=-123))
print(s.reverse(x=120))
print(s.reverse(x=1534236469))
