# week03-5.py 學習計畫 Sliding Window 第4題
# LeetCode 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        zeros = 0
        tail = 0
        ans = 0

        for head in range(N):
            if nums[head] == 0:
                zeros += 1

            while zeros > 1:
                if nums[tail] == 0:
                    zeros -= 1
                tail += 1

            ans = max(ans, head - tail + 1)

        return ans - 1
