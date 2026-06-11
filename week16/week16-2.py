class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        # now: 目前累積的數字組合
        # start: 下一個可以嘗試放進來的數字（避免重複選取、維持遞增順序）
        # k: 還需要選幾個數字
        # n: 目標總和還差多少
        def helper(now, start, k, n):
            # 成功條件：剛好選滿 k 個數字，且剩餘總和剛好為 0
            if k == 0 and n == 0:
                ans.append(list(now)) # 複製一份目前組合丟進答案
                return

            # 剪枝/失敗條件：選超過個數、總和爆掉，或是數字已經用完
            if k <= 0 or n <= 0 or start > 9:
                return

            # 從 start 開始嘗試 1 到 9 之間的數字
            for ii in range(start, 10):
                # 做出選擇，並往下遞迴
                # 下一次要試的數字是 ii + 1，個數少 1 個 (k - 1)，總和減少 ii (n - ii)
                helper(now + [ii], ii + 1, k - 1, n - ii)

        # 從空組合、數字 1 開始嘗試
        helper([], 1, k, n)
        return ans
