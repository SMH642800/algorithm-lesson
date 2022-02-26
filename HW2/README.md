###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW2 
# 概念題 :book: 
## 1. ![](https://i.imgur.com/KBkCpEd.png)
- O(**n^3**)
- c = 4
- n = 1
## 2. ![](https://i.imgur.com/fHvawqe.png)
- O(**n^2**)
- c = 3
- n = 0

:::success
解法 : 令 c = 最大項次方的係數 + 1 且 g(n) = f(n)的最高次方項，則方程式為 f(n) <= c * g(n)
:::

---

# 程式題 :「延續二元搜尋(Binary Search)應用」 :desktop_computer:
* 示範程式 (python)： **Binary Search**
```python=
def binary_search(data, key):
    left,right = 0, len(data)-1
    while left <= right:        
        mid = (left + right)//2
        if data[mid] < key:
            left = mid + 1
        elif data[mid] > key:
            right = mid -1
        else:
            return mid
    return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print( binary_search(data,6) ) 
```

:::    success
**若想練習更多有關二元搜尋的題目：[Binary Search - LeetCode](https://leetcode.com/tag/binary-search/)**
:::

## 3. 數列被轉置
* 題目：
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

---

:::info
解題思路 : 
先看看mid值是否為target，若不是則分成兩種情況，每種情況再各分成兩種情況:
1. 若mid < right則代表(mid ~ right)之間是有序的
    - 若target剛好在(mid ~ right)之間，則將left指標往mid右邊移動一格
    - 若target不在(mid ~ right)之間，則將right指標往mid左邊移動一格
2. 若mid > right，則代表(mid ~ right)之間並不是有序的，而(left ~ mid)則為有序的
    - 若target剛好在(left ~ mid)之間，則將right指標往mid左邊移動一格
    - 若target不在(left ~ mid)之間，則將left指標往右邊移動一格
:::
1. 程式碼 : 
``` python
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
```
2. 測試結果 :
![](https://i.imgur.com/LQDeCBT.png)
3. 花費時間 : 1 hr
4. 自己完成的程度 : 嘗試許久，最後上google找答案

## 4. 數字可能重複，回傳範圍
- 題目：
   - 一個排序好的數列，其中有些數字會重複，在其中找一個數字n，由於n可能重複，請回傳n的最小及最大index。若n沒有重覆，則回傳兩個n的index。若n沒有在數列，回傳兩個-1.
    - [34. Find First and Last Position of Element in Sorted Array - LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- Example 1:
    - Input: nums = [5,7,7,8,8,10], target = 8
    - Output: [3,4]
- Example 2:
    - Input: nums = [5,7,7,8,8,10], target = 5
    - Output: [0,0]
- Example 3:
    - Input: nums = [5,7,7,8,8,10], target = 6
    - Output: [-1,-1]

---

:::info
解題思路 : 分別使用lower_bound和upper_bound函式找出上限和下限。lower_bound返回的是第一个滿足條件的位置，而upper_bound返回的是第一个不滿足條件的位置
:::

1. 程式碼 : 
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找出target在list裡最小的ndex位置
        left = self.lower_bound(nums, target)   
        # 找出target在list裡最大的index再往右一個的位置
        right = self.upper_bound(nums, target)  
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
```
:::success
在python裡已有封裝好上述function功能的模組，名為bisect模組
:::
```python
class Solution(object):
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
```
2. 測試結果 : 
![](https://i.imgur.com/CPKOiZN.png)
3. 花費時間 : 1 hour
4. 自己完成的程度 : 嘗試許久，最後上google找答案

## 5. 猜數字遊戲
- 題目：
    - 提供一個guess(int n)函式讓你呼叫來猜數字，當
        - 你猜的數字過大時，guess()回傳 -1
        - 你猜的數字過小時，guess()回傳 1
        - 你猜的數字對時，guess()回傳 0
    - 請透過重複呼叫guess()用==最少的次數==來猜到數字。
    - 374. [Guess Number Higher or Lower - LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)

---

:::info
解題思路 : 利用binary search，來回縮小猜數字的範圍
:::
1. 程式碼 : 
```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while True:
            mid = (left+right)//2
            res = guess(mid)
            if res == -1:   # 數字過大，縮限右邊
                right = mid - 1   
            elif res == 1:   # 數字過小，縮限左邊
                left = mid + 1
            else:   # 數字剛好，回傳
                return mid
```
2. 測試結果 : 
![](https://i.imgur.com/ZmRfYPl.png)
3. 花費時間 : 20 min
4. 自己完成的程度 : 自己完成，花了點時間了解題意


# 本週心得
* 程式題前兩題相比前一周難度提高，嘗試許久後還是不行，所以只好上網查，第三題難度還可以，就是稍微有花點時間了解一下題義的部分
* 很喜歡這種先發影片再來上課的方式，因為若聽不懂的地方可以倒帶回去重複聽到會為止!
