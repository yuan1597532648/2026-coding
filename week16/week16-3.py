import math

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 1. 依據區間的「結束時間（右邊的 end）」大小進行升序排序
        # 結束得越早，留給後面區間的空間就越大（貪婪策略）
        intervals.sort(key=lambda x: x[1])

        ans = 0
        # 2. 設定一個初始的「前一個區間的結束時間」，先設為負無限大
        previous_end = -math.inf

        # 3. 逐一取出每個區間的 [start, end]
        for start, end in intervals:
            # 如果目前區間的起點大於或等於前一個區間的終點，代表沒有重疊
            if previous_end <= start:
                previous_end = end  # 更新目前的結束時間
            else:
                # 糟了！竟然重疊了！這段不能用，必須把它刪掉
                ans += 1

        return ans
