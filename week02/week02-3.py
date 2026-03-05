# week02-3.py 學習計畫 Two Pointers 第2題
# LeetCode 392. Is Subsequence
# 一個迴圈, 裡面同時有兩個 index 變數, 叫 two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        if N1 == 0: return True

        i = 0
        for k in range(N2):
            if s[i] == t[k]:
                i += 1
            if i == N1:
                return True

        return False
