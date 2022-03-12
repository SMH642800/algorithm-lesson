###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW4 
# 概念題 :book: 
## 1.  Selection Sort
![](https://i.imgur.com/xyZ7vAb.jpg)

- 題目 :
    - 請使用Selection sort排序，6,4,1,3,5。在四個回合中，每回合的Change of Flag數量為何？總共的Change of Flag數量為何？

---

- 解答 : 
    - 每回合的change of flag : 
        - 第一回合 : 2 (1,4,6,3,5)
        - 第二回合 : 1 (1,3,6,4,5)
        - 第三回合 : 1 (1,3,4,6,5)
        - 第四回合 : 1 (1,3,4,5,6)
    - 總共的change of flage數量 : 
        - 2+1+1+1 = 5

## 2. Quick Sort
![](https://i.imgur.com/QM5xF0G.jpg)

- 題目 :
    - 使用Quick排序7個數字，1,2,3,4,5,6,7，請說明每回合的pivot如何選擇，會有best case。請參考投影片33頁，畫出二元樹表示。
    - 呈上題，請說明每回合的pivot如何選擇，會有worstcase。請參考投影片33頁，畫出二元樹表示。
    
- 解答 : 
    - best case : 
      ![](https://i.imgur.com/Gu2Va3i.jpg)

    - worst case : 
      ![](https://i.imgur.com/8zpcvwF.jpg)

## 3. 2-D Ranking Finding
- 題目 : 
    - 平面上四個點，(1,1),(2,2),(3,3),(4,4)。請依照課本的方法，說明如何找出四個點的Ranking。(可配合畫圖表示)
- 解答 : 
    - ![](https://i.imgur.com/E5FB2X8.jpg)


---

# 程式題 : Two Pointers類型 :desktop_computer:

:::success
**若想練習更多有關Two Pointers類型的題目：[LeetCode](https://leetcode.com/tag/two-pointers/)**
:::

## 4. 回文Palindrome
* [125. Valid Palindrome - LeetCode](https://leetcode.com/problems/valid-palindrome/)
* 題目：
    - 判斷字串是否為回文，回文是指正讀與反讀都相同的字串，例如abcba,xyyx
        - 字串會先改為全小寫，並刪去空白。
        - 例子："A man, a plan, a canal: Panama"是回文
        - 原因：“amanaplanacanalpanama”

---

:::info
解題思路 : 
- 先利用正規表示式來過濾字串，再由left和right指標往中間縮減，一個一個檢查是否相等
:::
1. 程式碼 : 
``` python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 利用正規表示式，只留下字母和數字
        s = re.sub("[^a-zA-Z0-9]+", "", s) 
        # 字母大小轉換
        s = s.lower() 

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```
2. 測試結果 :
![](https://i.imgur.com/IqlZ3vj.png)
3. 花費時間 : 50 min
4. 自己完成的程度 : 自己完成，有上googel查正規表示式如何寫

## 5. Linked List是否存在Cycle
- [141. Linked List Cycle - LeetCode](https://leetcode.com/problems/linked-list-cycle/)
- 題目：
    - 判斷一個Linked List是否存在Cycle。

---

:::info
解題思路 : 
- 建立slow和fast指標，slow移動一個而fast移動兩個，當slow和fast交會時，則代表此linked list是有cycle的
- 注意 : 要先判斷linked是否為空的以及head.next是否為Null，並且每次都要判斷fast和fast.next是否為Null
:::

1. 程式碼 : 
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # 第一次:判斷linked list是否為空的或著只有一個
        # 第二次:判斷fast和fast的下一個是否為null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
2. 測試結果 : 
![](https://i.imgur.com/nU8OWwD.png)
3. 花費時間 : 35 min
4. 自己完成的程度 : 自己完成，有先上網查看linked list的用法


# 本週心得
- 課堂教的sorting部分，算是複習上學期的資料結構，所以還記的一些，但在quick sort的tree部分有點不太清楚是要怎麼劃分
- 程式題的部分，由於有給hint，所以在解題想法上不花太久的時間，反而大部分的時間都是在查一些語法的部分
