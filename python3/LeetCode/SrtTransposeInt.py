import re


class Solution:
    def myAtoi(self, s: str) -> int:
        # 土办法
        # str = str.lstrip()
        # if len(str) == 0:
        #     return 0
        # flag, f, res, over = True, str[0], 0, (1 << 31) - 1
        # if f == '-':
        #     flag = False
        #     over = 1 << 31
        # elif f == "+":
        #     pass
        # else:
        #     try:
        #         res = int(f)
        #     except Exception as e:
        #         return 0
        # for a in str[1:]:
        #     try:
        #         res = 10*res + int(a)
        #     except Exception as e:
        #         break
        #     if res > over:
        #         return over if flag else -over
        # return res if flag else -res
        # 正则表达式
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("-42"))
print(s.myAtoi("4139 with sdflkjs"))
print(s.myAtoi("wodie sdfls 985"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("3.1143"))
print(s.myAtoi("+1"))
print(s.myAtoi("2147483646"))
