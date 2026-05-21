import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 先用作弊的寫法示範一次
        # nums.sort(reverse=True) # 先大到小排好 O(N*logN)
        # return nums[k-1] # 第k大的數，是 0...k-1

        # 要用 Heap 資料結構，可以找出最小的數
        # heapq.heapify(nums) # 變成 heap 資料結構
        # while nums:
        #     print( heapq.heappop(nums) )

        # 最後用這個版本
        heapq.heapify(nums) # 變成 heap 資料結構 O(N)
        for i in range(len(nums) - k):
            heapq.heappop(nums) # 吐掉不用的小數

        return heapq.heappop(nums) # 剩下的那個，就是第 k 大的
