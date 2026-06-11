class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # 如果沒有任何氣球，不需要射任何箭
        if not points:
            return 0

        # 1. 氣球照「右邊界 (end)」大小來排序
        # 貪婪策略：優先照顧最早結束的氣球，這樣一箭射在它的右邊界上，能順便穿透最多其他氣球
        points.sort(key=lambda x: x[1])

        ans = 0
        # 2. 記錄前一發箭射出的位置，初始設為負無限大
        previous_end = float('-inf')

        # 3. 逐一取出每個氣球的 [start, end]
        for start, end in points:
            # 如果「目前的氣球起點」大於「前一發箭的位置」，代表前一發箭射不到這顆氣球了！
            if previous_end < start:
                # 氣球有距離哦！只好再多射 1 箭
                ans += 1
                # 更新這一箭的位置，直接射在當前氣球的右邊界 (end)
                previous_end = end

        return ans
