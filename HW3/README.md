###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW3 
# 概念題 :book: 
## 1. Insertion Sort
- 題目 :
    - 請依據課本推導方式，當5個數字用insertion sort排序，data movement的平均值為多少？
    - 請使用insertion sort排序 6,4,1,3,5。在四個回合中，每回合的data movement數量為何？總共的data movement數量為何？

---

- 解答 : 
    - n = 5帶入 f(n)=(n+8)(n-1)/2，所以 f(5)=13。
    - 第一回合 : 3次，第二回合 : 4次，第三回合 : 4次，第一回合 : 3次，共14次。

## 2. Binary Search
- 題目 :
    - 請參考投影片25頁與26頁，算出15個有序數列使用Binary Search，平均的比對次數為何？
    
- 解答 : log(15+1) = 4



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

:::success
**若想練習更多有關二元搜尋的題目：[Binary Search - LeetCode](https://leetcode.com/tag/binary-search/)**
:::

## 3. 完全平方數
* [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
* 題目：
    - 判斷一個正整數是否為完全平方數
    - 限制：不可使用sqrt()
* ex1:
    - Input: num = 16
    - Output: true
* ex2:
    - Input: num = 14
    - Output: false

---

:::info
解題思路 : 
利用binary search的概念，找出 **mid * mid** 值是否剛好等於Input值
:::
1. 程式碼 : 
``` python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid*mid > num:
                right = mid - 1
            elif mid*mid < num:
                left = mid + 1
            else:
                return True
        return False
```
2. 測試結果 :
![](https://i.imgur.com/IEAkalM.png)
3. 花費時間 : 5 min
4. 自己完成的程度 : 自己完成

## 4. 尋找字元
- [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
- 題目：
    - 給定一個target字元與一個字元序列，該序列按非遞減的順序，在序列中找出一個字元，而該字元是比target字元大的最小字元。字元大小順序是由a,b,c…z，Z之後再連回a,b,c…。
    - 舉例：
        - 字元序列為[‘a’, ‘b’]，而target字元為z，要在字元序列中找比z大的最小字元，答案是a。
    - ex1:
        - Input: letters = [“c”,“f”,“j”], target = “a”
        - Output: “c”
    - ex2:
        - Input: letters = [“c”,“f”,“j”], target = “c”
        - Output: “f”

---

:::info
解題思路 : 
- 當mid值大於target時，代表此mid值有可能是答案，因此right指標移到mid的位置
- 當mid值小於target時，代表此mid值不可能是答案，因此left指標移到mid+1的位置
- 當mid值剛好等於target時，則要再判斷mid+1是否等於target:
    - 若等於，則left指標向右移動2步
    - 若沒有，則回傳
:::

1. 程式碼 : 
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        // 先判斷target是否大於或等於list中最左邊的值
        if target >= letters[len(letters) - 1]:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        while left < right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if letters[mid+1] != target:
                    return letters[mid + 1]
                else:
                    left = mid + 1
            elif letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[left]
```
2. 測試結果 : 
![](https://i.imgur.com/Fy3OcAG.png)
3. 花費時間 : 25 min
4. 自己完成的程度 : 自己完成

## 5. 尋找山頂
- [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
- 題目：
    - 給一個array，其中會有一個數為山頂，在山頂之前的數字會漸漸增加，在山頂之後的數字會漸漸減少。請找出山頂的index值。
    - 請勿使用max()或index()，嘗試用二元搜尋法來作。
- ex1:
    - Input: arr = [0,1,0]
    - Output: 1
- ex2:
    - Input: arr = [0,2,1,0]
    - Output: 1

---

:::info
解題思路 : 先找出mid值，再判斷是否符合題意
:::
1. 程式碼 : 
```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            // 若mid是在山頂的左側
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            // 若mid是在山頂的右側
            elif arr[mid] < arr[mid - 1]:
                right = mid - 1
            else:
                return mid
```
2. 測試結果 : 
![](https://i.imgur.com/jVguAkh.png)
3. 花費時間 : 10 min
4. 自己完成的程度 : 自己完成


# 本週心得
* 程式題相較以往，簡單許多，很快就做出來了，反而是概念題的部分想得比較久一點
