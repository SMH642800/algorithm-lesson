"""
 題目：
    - 原有一個數字不重複的遞增數列。
    - 現有可能將此數列旋轉i個，例如原本是：0,1,2,3,4；旋轉2個後就是2,3,4,0,1。
    - 在此數列中，尋找數字n，若存在則回傳其index值；若無則回傳-1
    - [33. Search in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* Example 1:
    - Input: nums = [4,5,6,7,0,1,2], target = 0
    - Output: 4
* Example 2:
    - Input: nums = [4,5,6,7,0,1,2], target = 3
    - Output: -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 若mid < right，則代表(mid ~ right)之間是有序的，沒有受到rotate的影響
            if nums[mid] < nums[right]:
                # 若target剛好在(mid ~ right)之間，則將left指標往mid右邊移動一格
                if (target > nums[mid]) and (target <= nums[right]):
                    left = mid + 1
                # 若target不在(mid ~ right)之間，則將right指標往mid左邊移動一格
                else:
                    right = mid - 1
            # 若mid > right，則代表(mid ~ right)之間並不是有序的，受到rotate的影響
            else:
                # 若target剛好在(left ~ mid)之間，則將right指標往mid左邊移動一格
                if (target < nums[mid]) and (target >= nums[left]):
                    right = mid - 1
                # 若target不在(left ~ mid)之間，則將left指標往右邊移動一格
                else:
                    left = mid + 1
        return -1
