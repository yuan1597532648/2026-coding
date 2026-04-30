# week10-6.py 學習計畫 Binary Tree - DFS 第5題
# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# 找到中間 ZigZag 左右左右 or 右左右左 最長的那個

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0  # 整個的答案

        def helper(root):
            if root == None:
                return 0, 0  # 左邊最長、右邊最長

            # Lans1, Lans2 代表左子節點回傳的 (左最長, 右最長)
            Lans1, Lans2 = helper(root.left)
            # Rans1, Rans2 代表右子節點回傳的 (左最長, 右最長)
            Rans1, Rans2 = helper(root.right)

            # 更新全域答案：
            # 當前點往左走，接的是左邊小朋友的「右邊最長」(Lans2 + 1)
            # 當前點往右走，接的是右邊小朋友的「左邊最長」(Rans1 + 1)
            self.ans = max(self.ans, Lans2 + 1, Rans1 + 1)

            # 回傳給上一層父節點：
            # (我往左走能多長, 我往右走能多長)
            return Lans2 + 1, Rans1 + 1

        helper(root)

        # 因為程式計算的是「節點數量」，題目要的是「路徑長度」(邊的數量)
        # 所以最後答案要減 1
        return self.ans - 1
