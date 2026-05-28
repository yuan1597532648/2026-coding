# week14-2a.py 學習計畫 1D DP 第1題 Easy
# LeetCode 1137. N-th Tribonacci Number
class Solution:

    def tribonacci(self, n: int) -> int:
        # 必須先把 n 為 0, 1, 2 的狀況攔截掉，避免後面陣列範圍出錯
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        # 初始化陣列
        a = [0, 1, 1] + [0] * n

        # 從索引 3 開始動態規劃計算
        for i in range(3, n + 1):
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]

        # print(a)
        return a[n]
