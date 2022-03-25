"""
- 題目:
    - 已知一個數列，每個數字代表可以向後跳的最大距離。
    - 假設一定可以在跳躍數次後到達最終點。
    - 求到達終點的許多跳法中，最少的跳躍次數。
-Example 1:
    - Input: nums = [2,3,1,1,4]
    - Output: 2
    - Explanation: The minimum number of jumps to reach the last index is 2. 
	Jump 1 step from index 0 to 1, then 3 steps to the last index.
- Example 2:
    - Input: nums = [2,3,0,1,4]
    - Output: 2
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = 0  # 設立上一步所有的index，下一步能走到的範圍
        step = 0
        while right < len(nums) - 1:
            far_index = 0  
            for i in range(left, right + 1):
                # 在範圍裡面每一個index能走到最遠的位置
                far_index = max(far_index, i + nums[i])
            # 設定下一個能走到的範圍
            left = right + 1
            right = far_index
            step += 1
        return step