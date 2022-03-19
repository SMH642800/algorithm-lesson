"""
- 已知一個數列，每個數字代表可以向後跳的最大距離，請判斷是否可從起點，多次跳躍後，可到達最終點。
    - 範例：
        - 輸入：3,2,4,2,4
        - 輸出：true
        - 說明
            - 由index 0的位置，跳躍3個數至index 3。
            - 從index 3的位置，跳躍1個數，最到達最終點。
    - 範例：
        - 輸入：3,2,1,0,4
        - 輸出：false
        - 說明
            - 由index 0,1,2最遠只能跳到index 3。
            - 由index 0,1,2最遠只能跳到index 3。
"""


# method 1: 
class Solution:
        def canJump(self, nums: List[int]) -> bool:
            target_index = len(nums) - 1
            # 從倒數第二個index往前一個個檢查
            for index in range((len(nums)-2), -1, -1):
                # 若能到達則把target_index替換掉
                if (index+nums[index] >= targetIndex):
                    target_index = index
            # 若能走到第一個index，代表能夠從第一個index走到最後一個index
            if target_index == 0:  
                return True
            else:
                return False


# method 2:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far_reach_index = 0   # 最遠能達到的index
        # enumerate(sequence: list, [start=0]):
        # seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
        for index, number in enumerate(nums):
            if index > far_reach_index:
                return False
            far_reach_index = max(far_reach_index, index + number)
        return True