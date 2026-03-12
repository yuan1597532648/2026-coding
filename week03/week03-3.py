# week03-3.py 學習計畫 Sliding Window 第2題
# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count
        N = len(s)

        for i in range(k, N):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1

            ans = max(ans, count)

        return ans
