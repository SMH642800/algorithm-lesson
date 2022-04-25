###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW7
# 概念題 :book: 
## 1.  knapsack problem背包問題(Ch3)
- 題目 : 
    - 有四件物品，編號由1到4，物品重量依序為20,40,10,30。物品價值依序為100,60,30,60。背包最大限重為80。請說明要放哪些東西(可以放部分)，可以讓背包內物品價值總合最大。

---

- 解答 : 
    - ==**編號: (value/weight)**==
        - 1: (100/20) = 5
        - 2: (60/40) = 1.5
        - 3: (30/10) = 3
        - 4: (60/30) = 2
    - 因此優先度為: 1 -> 3 -> 4 -> 2
    - 所以內容物為: 
        - 1: 20 (全部)
        - 2: 20 (取一半)
        - 3: 10 (全部)
        - 4: 30 (全部)
        - 背包內總價值為: 100 + 30 + 30 + 60 = 220



## 2. Closest Pair Problem
- 題目 :
    - 請說明Closest Pair Problem，每回合的合併過程？(可參考PPT13頁)

---

- 解答 : 
    ![](https://i.imgur.com/426oqNG.jpg)
    - 在x = L~(L-d)的範圍內所有的點令為P點，而他們的 *y-value* 被稱為 $y_p$。
    - 對每一個P，找出在x = L~(L+d)範圍內且其 *y-value* 是在($y_p$+d) ~ ($y_p$-d)之間的所有點。
    - P點與這些找出的點進行距離計算，算出的值稱為 **d'**，若 **d'** < **d**，則更新d的value => ==d = d'==。
    - 重複上述動作，將所有的P點全部掃完一遍後，d值即為答案。
    
## 3. Convex Hull Problem
- 題目 : 
    - 請說明Convex Hull Problem，
    (1)為何不直接用sort來得到polygon，而要採用merge？
    (2)請說明如何將polygon，修改成convex hull？

---

- 解答 : 
    1. 由於利用向量大小將點進行sort來得到polygon的時間複雜過高(==O(nlogn)==)，因此採用merge的方式來達到一樣的目的，但merge方法的時間複雜度更低(==O(n)==)
    2. 利用==Graham scan==一個一個檢查節點是否為==reflex angles (角度>180)==，若是則刪除此節點，最後即形成convex hull。


---

# 程式題 : [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) :desktop_computer:


## 4. 將linked list的數列排序
- [148. Sort List](https://leetcode.com/problems/sort-list/)
- 給定一個linked list的數列，其中的數字並未排序，請將數列排序後，回傳排序好數列的linked list。
:::success
**Hint**：初學者可採用將linked list轉為array後來排序。高手建議可嘗試用merge sort，以divide and conquer的概念來作。
:::

---

:::info
解題思路 : 
1. linked list -> array，array -> linked list
2. 先將linked list分成左右兩堆，一直遞迴分堆，然後在一個個合併起來，合併的過程中利用2-way merging的想法，去對左右兩堆進行比較大小合併

==[解說影片 : Sort List - Merge Sort - Leetcode 148 (Python)](https://youtu.be/TGveA1oFhrc)==
:::
1. 程式碼 : 
``` python
# method 1 : linked list -> array，array -> linked list

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def convert_to_listnode(l, head=None, current=None, index=0):
            if(index > len(l)-1):
                return head

            if(head == None):
                head = ListNode(l[index])
                current = head
                return convert_to_listnode(l, head, current, index+1)

            next_node = ListNode(l[index])
            current.next = next_node
            current = next_node
            index += 1
            return convert_to_listnode(l, head, current, index)
        
        
        if not head or not head.next:
            return head
        
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        dummy = convert_to_listnode(arr)
        
        return dummy
    
===================================================================

# method 2 : merge

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # split the list into two halfs
        left = head
        right = self.getMid(head)  # 找到linked list的中間點
        tmp = right.next
        right.next = None  # 左堆建立完成
        right = tmp  # 右堆建立完成
        
        # recursive to merge the result
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        if h1:
            tail.next = h1
        if h2:
            tail.next = h2
            
        return dummy.next

```
2. 測試結果 :
![](https://i.imgur.com/rM8Qv6M.png)
3. 花費時間 : 1 hr 30 min
4. 自己完成的程度 : method 1 -> 自己完成、method 2 -> 上網googel看解題影片

## 5. 將排序好的數列轉為二元搜尋樹
- [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
- 已知一個排序好的數列，請將每個數字為一個點，建構一個二元搜尋樹。
- 例如：數列為[-10,-3,0,5,9]時，可轉為以下的二元搜尋樹(兩種皆可)
![](https://i.imgur.com/cWyh0G8.png)
![](https://i.imgur.com/32w3wpC.png)
:::success
**Hint**：取數列的中間值為root，並將數列分為左右兩個數列，用左數列建立root的左子樹，用右數列建立root的右子樹。
:::

---

:::info
解題思路 : 
1. 取數列的中間值為root，分成左右兩堆，在左右兩堆之中再去各別找出左右兩堆的root以及左子堆和右子堆
2. 一直不斷的遞迴下去，直到left指標超過right指標，代表已經沒有值可以建構tree了，因此就回傳null值回去
3. 不斷往上一層進行結果合併，即可得到解答
:::

1. 程式碼 : 
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        def getNode(l: int, r: int):
            if l > r: 
                return None   

            mid = (l + r) // 2  
            root = TreeNode(nums[mid])   # 取得中間點為root
            root.left = getNode(l, mid - 1)  # 分成左堆後再去遞迴函式
            root.right = getNode(mid + 1, r) # 分成右堆後再去遞迴函式
            return root
        
        return getNode(0, len(nums) - 1)
```
2. 測試結果 : 
![](https://i.imgur.com/IKa0JNP.png)
3. 花費時間 : 50 min
4. 自己完成的程度 : 上網google才會


# 本週心得
- 程式題的部分，由於是第一次接觸tree的題目，還不熟悉tree在程式語言裡面的用法，所以寫起來特別花時間去理解
- 覺得程式題的難度突然增加很多，有點難以適應，看來要多花一點時間去練習才行 (但這學期的課程很滿，實在很難再擠出時間來額外練習，有點遺憾)
