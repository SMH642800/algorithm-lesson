###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW1 
# 概念題 :book: 
## 1. 本週影片中提到的NP-complete問題有那些?
* 	0/1 Knapsack problem
* 	Traveling salesperson problem
* 	Partition problem
* 	Art gallery problem
## 2. 請上網找一個老師沒說過的NP-complete問題，並舉個例子說明該問題的輸入與輸出。
* Subset sum problem (子集合加總問題)。
     - 給一個整數集合 -> Input = {-7, -3, -2, 5, 8}，問是否存在子集合為0的集合? 
     - 答案為Yes，Output = {-3, -2, 5}的和為0。

---

# 程式題 :「二元搜尋(Binary Search)應用」 :desktop_computer:
* 示範程式 (python)： **Binary Search**
```python
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

## 3. 二元搜尋應用 : 當數字可以重複
* 題目：在排序好的數列中，其中數字有可能重覆，請修改原程式，可以回傳最小的index值
* Example 1:
    - Input: [1,3,3,6], 3
    - Output: 1
    - 說明：3有在數列中出現兩次，較小的index為1
* Example 2:
    - Input: [1,3,3,6], 2
    - Output: 1
    - 說明：2沒有在數列中，輸出-1
* Example 3:
    - Input: [1, 2, 3, 6, 6, 6, 7, 8, 9], 6
    - Output: 3
    - 說明：6在數列中出現3次，最小的index為3

---

1. 程式碼 : 
``` python
def binary_search(data: list, left: int, right: int, key: int):
    while left <= right:
        mid = (left + right)//2
        if int(data[mid]) < key:
            left = mid + 1
        elif int(data[mid]) > key:
            right = mid - 1
        else:
            # 當第一次找到key的index值時，往前找看看是否還有更小的key的index值
            index_num = binary_search(data, left, mid-1, key)
            if index_num == -1:   # 若沒有更小的index值，則回傳原本第一次的值
                return mid
            else:   # 若有更小的index值，則回傳更小的值
                return index_num
    return -1


def main():
    data = input().split()
    key = int(input())
    left, right = 0, len(data) - 1
    print(binary_search(data, left, right, key))


if __name__ == "__main__":
    main()
```
2. 測試結果 :
![](https://i.imgur.com/6JVSRtm.png)

3. 花費時間 : 25 min
4. 自己完成的程度 : 完全靠自己

:::info
**挑戰 :** 若是要找重覆數字==最大的index值==如何改?
:::

## 4. 二元搜尋應用 : 找數字該插入的位置
- 題目：
    - 給一個排序好的數列，在其中搜尋n，若是找到，則回傳n的index，==若無則回傳該插入的位置==。
    - [35. Search Insert Position - LeetCode](https://leetcode.com/problems/search-insert-position/)
- Example 1:
    - Input: [1,3,5,6], 5
    - Output: 2
    - 說明：5有在數列中，index為2
- Example 2:
    - Input: [1,3,5,6], 2
    - Output: 1
    - 說明：2沒有在數列中，插入在index為1的位置

---

1. 程式碼 : 
```python
def binary_search(data: list, left: int, right: int, key: int):
    curr_index = 0   # 記錄最近一次的index值
    while left <= right:
        mid = (left + right)//2
        if int(data[mid]) < key:
            curr_index = mid + 1   
            left = mid + 1
        elif int(data[mid]) > key:
            curr_index = mid
            right = mid - 1
        else:
            return mid
    return curr_index


def main():
    data = input().split()
    key = int(input())
    left, right = 0, len(data) - 1
    print(binary_search(data, left, right, key))


if __name__ == "__main__":
    main()
```
2. 測試結果 : 
![](https://i.imgur.com/2eeDppL.png)
![](https://i.imgur.com/Ppa458r.png)

3. 花費時間 : 10 min
4. 自己完成的程度 : 完全靠自己

## 5. 二元搜尋應用 : 找出最早出問題的版本
- 題目：
    - 已知一個程式，從開發至今有n個版本，但是發現最新的版本是錯的，有可能更早的版本就開始出錯了，錯誤一直延續到最新版。題目提供isBadVersion(n)函式，可以測試第n個版本是否有錯，請利用重覆呼叫此函式，找到最早出問題的版本
    - [278. First Bad Version - LeetCode](https://leetcode.com/problems/first-bad-version/)
- ex1:
    - 若是呼叫isBadVersion(2) = False
    - 呼叫isBadVersion(3) = False
    - 呼叫isBadVersion(4) = True
    - 呼叫isBadVersion(5) = True
    - 則找到最早出問題的版本為4
- ex2:
    - 若是呼叫isBadVersion(6) = False
    - 呼叫isBadVersion(7) = False
    - 呼叫isBadVersion(8) = True
    - 呼叫isBadVersion(9) = True
    - 則找到最早出問題的版本為8

---

1. 程式碼 : 
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```
2. 測試結果 : 
![](https://i.imgur.com/I9EfXiI.png)

3. 花費時間 : 10 min
4. 自己完成的程度 : 看不太懂題意，所以上網google後才會

## 6. 二元搜尋應用 : 開根號後的整數部分
- 題目：
    - 根號2是1.414…，整數部分是1。根號7是2.645…，整數部分是2。
    - 給定一個n，求開根號後的整數部分
    - 限制：不能呼叫內建函式sqrt()
    - ex1: input: 2 , output: 1
    - ex2: input: 7 , output: 2
    - ex3: input: 9 , output: 3

---

1. 程式碼 :  
```python          
import math
from math import sqrt


def binary_search(num: int):
    x = sqrt(num)
    mid = num/2.0
    left, right = 0.0, num*1.0
    while abs(mid-x) > 0.0001:
        if mid*mid > num:
            right = mid
            mid = (left+right)/2
        else:
            left = mid
            mid = (left+right)/2
    return int(mid)


def main():
    num = int(input())
    print(binary_search(num))


if __name__ == "__main__":
    main()
```
2. 測試結果 : 
![](https://i.imgur.com/kYtJRj9.png)

3. 花費時間 : 30 min
4. 自己完成的程度 : 上網google後才會


# 本週心得
* 程式題前兩題雖然要花點時間想，但其實時做下來覺得難易度適中，很快就做出來了。但第三、四題就有點看不太懂題意了，所以只好上網查，不過好在查完之後也不太難理解。
* 很喜歡這種先發影片再來上課的方式，因為若聽不懂的地方可以倒帶回去重複聽到會為止!
