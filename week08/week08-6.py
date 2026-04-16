# week08-6.py 學習計畫 Binary Search 最難的第4題
# LeetCode 875. Koko Eating Bananas

from typing import List
from bisect import bisect_left

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 準備一個函式 helper(ans) 看答案對不對
        def helper(k):
            # 1小時吃 k 個香蕉，看香蕉能否在 h 小時吃完
            total = 0  # 你猜 k，它會用多少時間

            for pile in piles:  # 很多堆香蕉，逐一檢查
                total += pile // k  # 要吃掉這堆香蕉 pile 要花多少時間
                if pile % k > 0:
                    total += 1  # 有餘數，再多 1 小時

            return total <= h  # 符合條件（在 h 小時內吃完）

        return bisect_left(range(1, max(piles)), True, key=helper) + 1
