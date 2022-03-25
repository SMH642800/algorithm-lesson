"""
- [11. Container With Most Water - LeetCode]
- 題目：
    - 一個水槽有多個等間隔的隔板，任兩個隔板可以擋住一定份量的水。
    - 如下圖所示，由紅色的兩個隔板，所能擋住的水量為兩隔板的間隔乘上較矮隔板高度。
    - 題目會給定一個數列，分別代表隔板的高度。
    - 請找出由兩個隔板可擋住的最大水量。

- Example 1 : 
    - Input: height = [1,8,6,2,5,4,8,3,7]
    - Output: 49
    - Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
	In this case, the max area of water (blue section) the container can contain is 49.
- Example 2 :
    - Input: height = [1,1]
    - Output: 1
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 計算目前能得出的area面積
            now_area = min(height[left], height[right]) * (right - left)
            # 跟之前儲存的max_area進行比較大小，留下最大值
            max_area = max(max_area, now_area)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_area     