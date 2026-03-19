# week04-2.py 學習計畫 prefix sum 第1題
# LeetCode 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain)
        ans = H = 0

        for i in range(N):
            H += gain[i]
            ans = max(ans, H)

        return ans
