# 演算法作業 HW1
# 概念題 :book:
## 1. 本週影片中提到的NP-complete問題有那些?
* 	0/1 Knapsack problem
* 	Traveling salesperson problem
* 	Partition problem
* 	Art gallery problem
## 2. 請上網找一個老師沒說過的NP-complete問題，並舉個例子說明該問題的輸入與輸出。
* Subset sum problem (子集合加總問題)。
* 給一個整數集合，Input = {-7, -3, -2, 5, 8}，是否存在子集合為0的集合? 
* 答案為Yes，Output = {-3, -2, 5}的和為0。
# 程式題(二元搜尋(Binary Search)應用) :desktop_computer:
## 3. 二元搜尋應用 : 當數字可以重複
1. 程式碼 : 
``` python
def binary_search(data: list, left: int, right: int, key: int):
    while left <= right:
        mid = (left + right)//2
        if int(data[mid]) < key:
            left = mid + 1
        elif int(data[mid]) > key:
            right = mid -1
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

## 4. 二元搜尋應用 : 找數字該插入的位置
1. 程式碼 : 
```python
def binary_search(data: list, left: int, right: int, key: int):
    curr_num = 0   # 記錄最近一次的index值
    while left <= right:
        mid = (left + right)//2
        if int(data[mid]) < key:
            curr_num = mid + 1   
            left = mid + 1
        elif int(data[mid]) > key:
            curr_num = mid
            right = mid - 1
        else:
            return mid
    return curr_num


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

3. 花費時間 : 10 min
4. 自己完成的程度 : 完全靠自己

## 5. 二元搜尋應用 : 找出最早出問題的版本
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
