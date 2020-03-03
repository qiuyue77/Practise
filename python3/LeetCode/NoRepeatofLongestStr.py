# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         subStr = ''
#         strNum = 0
#         for x in s:
#             if x in subStr:
#                 strNum = max(strNum, len(subStr))
#                 subStr = subStr[subStr.index(x):]
#                 continue
#             else:
#                 subStr += x
#                 strNum = max(strNum, len(subStr))
#         return strNum


# a = Solution()
# print(a.lengthOfLongestSubstring(" "))
# print(a.lengthOfLongestSubstring(""))
# print(a.lengthOfLongestSubstring("aabaab!bb"))
# print(a.lengthOfLongestSubstring("bbbb"))
# print(a.lengthOfLongestSubstring("pwwkew"))
# print(a.lengthOfLongestSubstring("dvdf"))
# print(a.lengthOfLongestSubstring("aab"))

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


a = Solution()
# print(a.lengthOfLongestSubstring(" "))
# print(a.lengthOfLongestSubstring(""))
print(a.lengthOfLongestSubstring("aabaab!bb"))
# print(a.lengthOfLongestSubstring("bbbb"))
# print(a.lengthOfLongestSubstring("pwwkew"))
# print(a.lengthOfLongestSubstring("dvdf"))
# print(a.lengthOfLongestSubstring("aab"))
