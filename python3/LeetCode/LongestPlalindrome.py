class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) == 0:
        #     return ''
        # final_str = s[0]
        # temp_str = ''
        # if len(s) == 2 and s[0] == s[1]:
        #     return s
        # for n in range(0, len(s)-1):
        #     # 相邻相同的回文
        #     if s[n] == s[n+1]:
        #         temp_str = s[n:n+2]
        #         final_str = final_str if len(
        #             final_str) > len(temp_str) else temp_str
        #         loop_time = min(n, len(s)-n-3)
        #         if n >= 1:
        #             for x in range(loop_time+1):
        #                 if s[n-1-x] == s[n+2+x]:
        #                     temp_str = s[n-1-x:n+3+x]
        #                     final_str = final_str if len(
        #                         final_str) > len(temp_str) else temp_str
        #                 else:
        #                     break
        #     if n >= 1:
        #         # 相邻不相同的回文
        #         if s[n-1] == s[n+1]:
        #             temp_str = s[n-1:n+2]
        #             final_str = final_str if len(
        #                 final_str) > len(temp_str) else temp_str
        #             loop_time = min(n-2, len(s)-n-3)
        #             if n >= 2:
        #                 for x in range(loop_time+1):
        #                     if s[n-2-x] == s[n+2+x]:
        #                         temp_str = s[n-2-x:n+3+x]
        #                         final_str = final_str if len(
        #                             final_str) > len(temp_str) else temp_str
        #                     else:
        #                         break
        if len(s) == 0:
            return ''
        final_str = s[0]
        temp_str = ''
        s = '#' + '#'.join(s) + '#'
        for n in range(1, len(s)-1):
            if s[n-1] == s[n+1]:
                temp_str = s[n-1:n+2]
                final_str = final_str if len(
                    final_str) > len(temp_str) else temp_str
                loop_time = min(n-2, len(s)-n-3)
                for x in range(loop_time+1):
                    if s[n-2-x] == s[n+2+x]:
                        temp_str = s[n-2-x:n+3+x]
                        final_str = final_str if len(
                            final_str) > len(temp_str) else temp_str
                    else:
                        break
        return ''.join(final_str.split('#'))


S = Solution()
print("aba-", S.longestPalindrome('babad'))  # abad
print("bb-", S.longestPalindrome('cbbd'))  # bb
print('bcddcbcddcb-', S.longestPalindrome('abcddcbcddcb'))  # bcddcbcddcb
print('aaaaa-', S.longestPalindrome('aaaaa'))  # aaaaa
print('aaaa-', S.longestPalindrome('aaaa'))
print('bb-', S.longestPalindrome('abb'))
