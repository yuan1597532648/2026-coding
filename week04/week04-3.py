# week04-3.py More Challenges ªºÂ²³æÃD
# LeetCode 3866. First Unique Even Element

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        N = len(nums)
        H = [0] * 200
        for i in range(N):
            H[ nums[i] ] += 1

        for i in range(N):
            if nums[i] % 2 == 0 and H[ nums[i] ] == 1:
                return nums[i]

        return -1
