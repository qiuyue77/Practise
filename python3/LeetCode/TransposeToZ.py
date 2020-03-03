class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        flag = -1
        ind = 0
        for n in s:
            res[ind] += n
            if not ind or ind == numRows - 1:
                flag = -flag
            ind += flag
        return ''.join(res)


solution = Solution()
print(solution.convert(s="LEETCODEISHIRING", numRows=3))
print(solution.convert(s="LEETCODEISHIRING", numRows=4))
