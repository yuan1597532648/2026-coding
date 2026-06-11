class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 如果輸入是空字串，直接回傳空陣列
        if not digits:
            return []

        # 建立電話號碼按鍵與字母的對照表
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ans = []

        # 定義回溯法/DFS 函數
        def backtrack(index, path):
            # 如果目前組合的長度已經等於輸入數字的長度，代表找到一個完整組合了
            if index == len(digits):
                ans.append("".join(path))
                return

            # 取出當前數字對應的所有可能字母
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                path.append(letter)      # 做出選擇
                backtrack(index + 1, path) # 遞迴處理下一個數字
                path.pop()               # 撤銷選擇（回溯）

        # 從第 0 個數字開始，初始路徑為空陣列
        backtrack(0, [])
        return ans
