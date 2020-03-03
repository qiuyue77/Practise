class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50,
             'XC': 80, 'C': 100, 'CD': 300, 'D': 500, 'CM': 800, 'M': 1000}
        return sum(d.get(s[max(i-1, 0): i+1], d[n]) for i, n in enumerate(s))


s = Solution()
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('III'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))
