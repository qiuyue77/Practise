class Solution:
    def maxArea(self, height) -> int:
        res = 0
        fsur = 0
        bsur = len(height) - 1
        while fsur <= bsur:
            if height[fsur] >= height[bsur]:
                res = max(res, (bsur-fsur)*height[bsur])
                bsur -= 1
            else:
                res = max(res, (bsur-fsur)*height[fsur])
                fsur += 1
        return res


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([2, 3, 10, 5, 7, 8, 9]))
print(s.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
