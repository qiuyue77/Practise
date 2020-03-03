class Solution:
    def inToRoma(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC",
                  "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ''
        while index < 13:
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res


s = Solution()
print(s.inToRoma(1388))
print(s.inToRoma(10))
print(s.inToRoma(9))
print(s.inToRoma(99))
