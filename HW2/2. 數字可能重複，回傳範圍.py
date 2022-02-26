"""
- 題目：
   - 一個排序好的數列，其中有些數字會重複，在其中找一個數字n，由於n可能重複，請回傳n的最小及最大index。若n沒有重覆，則回傳兩個n的index。若n沒有在數列，回傳兩個-1.
    - [34. Find First and Last Position of Element in Sorted Array - LeetCode]
- Example 1:
    - Input: nums = [5,7,7,8,8,10], target = 8
    - Output: [3,4]
- Example 2:
    - Input: nums = [5,7,7,8,8,10], target = 5
    - Output: [0,0]
- Example 3:
    - Input: nums = [5,7,7,8,8,10], target = 6
    - Output: [-1,-1]
"""


# 當mid < target時，才移動left指標
def lower_bound(data: list, target: int):
    left, right = 0, len(data)
    while left < right:
        mid = (right - left)//2 + left
        if int(data[mid]) < target:
            left = mid + 1
        else:
            right = mid
    return left


# 當mid <= target時，就移動left指標
def upper_bound(data: list, target: int):
    left, right = 0, len(data)
    while left < right:
        mid = (right - left)//2 + left
        if int(data[mid]) <= target:
            left = mid + 1
        else:
            right = mid
    return left


def binary_search_range(data: list, target: int):
    left = lower_bound(data, target)   # 找出target在list裡最小index的值
    right = upper_bound(data, target)   # 找出target在list裡最大index再往右一個的值
    if left == right:
        return [-1, -1]
    return [left, right - 1]


def main():
    data = input().split()
    target = int(input())
    print(binary_search_range(data, target))


if __name__ == "__main__":
    main()


"""
//Method 1 :
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower_bound(nums, target)   # 找出target在list裡最小index的值
        right = self.upper_bound(nums, target)   # 找出target在list裡最大index再往右一個的值
        if left == right:
            return [-1, -1]
        return [left, right - 1]
        
        
    # 當mid < target時，才移動left指標
    def lower_bound(self, nums: list, target: int):
        left, right = 0, len(nums)
        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


    # 當mid <= target時，就移動left指標
    def upper_bound(self, nums: list, target: int):
        left, right = 0, len(nums)
        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


// Method 2 :
class Solution(object):
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

"""