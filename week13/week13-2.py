from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # 長, 寬
        queue = deque()

        # 把爛掉的橘子，放入 queue
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue.append( (i, j, 0) )

        ans = 0 # 紀錄花費的時間

        while queue:
            i, j, t = queue.popleft()
            ans = t # 更新爛掉的時間！

            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if ii < 0 or jj < 0 or ii >= M or jj >= N: continue # 超過邊界，下一位

                # 如果這格是還沒爛掉的橘子，可感染它！
                if grid[ii][jj] == 1:
                    grid[ii][jj] = 2 # 把它變成爛橘子（這樣就不需要額外的 visited 集合了）
                    queue.append( (ii, jj, t+1) ) # 將在 t+1 時爛掉

        # 最後檢查地圖上是否還有新鮮橘子沒被感染到
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1

        return ans
