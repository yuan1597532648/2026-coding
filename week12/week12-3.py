# week12-3.py 學習計畫 Graph - DFS
# LeetCode 547. Number of Provinces 探討有多少個「幾群」連通的
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected) # 先知道有多少個 Nodes
        visited = set() # 走過的方，不要再走

        def helper(now): # 函式呼叫函式，因為 function stack 就是一種 DFS
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)

        ans = 0 # 有「幾群」是連通的
        for i in range(N): # 全部 node 掃一次
            if i not in visited: # 沒有去過的話
                ans += 1 # 代表是新的一群
                helper(i) # 用函式呼叫函式，努力把它的鄰居、鄰居的鄰居...全都走過
        return ans
