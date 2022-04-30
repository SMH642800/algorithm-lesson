###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW8
# 概念題 :book: 
## 1.  Voronoi Diagram
- 題目 : 
    - 請畫出下圖兩個VD合併結果，畫出新建立的線段(註明為哪兩點的中垂線)，並說明簡述流程。
    ![](https://i.imgur.com/0ixTlA3.png)

---

- 解答 : 
    1. 先找出左邊VD的convex hull和右邊VD的convex hull，我們能得知==P1==和==P5==及為要新增HP的兩個起始點
        ![](https://i.imgur.com/mG1OxIk.jpg)
    2. 再由這兩個起始點去找出HP線 ( <span class="red">紅線: 中垂線</span>、<span class="blue">藍線: 兩點的相連線</span>、<span class="green">綠線: HP線</span>)
    
        <style>
            .blue {color: blue;}
            .red {color: red;}
            .green {color: green;}
        </style>
        
        1. 先畫出P1、P5的中垂線為b15，而b15和b45交錯，其轉折點為a1
        2. 再來畫出P1、P4的中垂線為b14，而b14和b13交錯，其轉折點為a2
        3. 再來畫出P4、P3的中垂線為b34，而b34和b46交錯，其轉折點為a3
        4. 再來畫出P3、P6的中垂線為b36，而b36和b23交錯，其轉折點為a4
        5. 再來畫出P6、P2的中垂線為b26，而b26從轉折點a4開始往外畫
        6. 這些中垂線集合起來便是==HP==
        ![](https://i.imgur.com/tmPqouJ.jpg)






## 2. Voronoi Diagram的應用
- 題目 :
    - 請說明The Euclidean all nearest neighbor problem為何，以及如何應用VD來解此問題？
---

- 解答 : 
    - 在平面上n有個點，找出所有點的closest neighbor
    - 由於**VD性質: 距離點$P_i$最接近的點$P_j$==一定==會跟$P_i$共用一條VD的邊**，因此可以利用此特性來檢查$P_i$周圍的所有的VD邊來得到兩點之間的距離值，再依每個點所提供的距離值來找出$P_i$的closest neighbor
    
## 3. FFT
- 題目 : 
    - 當輸入為：{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}，請說明如何應用FFT得到結果(只須說明計算過程，不用算出結果)？

---

- 解答 : 
    1. n = 16 > 2，所以將這16個數字分成奇、偶兩堆
    2. 奇、偶兩堆的數量 n = 8 > 2，所以繼續將兩堆各分奇、偶兩堆，持續分堆下去直到每堆的數量 n = 2 為止
    3.  將奇、偶兩堆的結果計算出來: $A_0$ = $a_0$ + $a_1$ 、 $A_1$ = $a_0$ - $a_1$
    4.  將奇、偶兩堆的結果合併: $A_0$ = $c_0$ + $d_0$ 、 $A_1$ = $c_1$ + $d_1$* (-i) 、 $A_2$ = $c_0$ - $d_0$ 、 $A_3$ = $c_1$ - $d_1$* (-i)
    5.  之後就一路將前面所有的奇、偶兩堆的結果合併起來，最終就能得到答案


---

# 程式題 : [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) :desktop_computer:


## 4. 由Preorder與Inorder建構二元樹
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- 關於如何由Preorder與Inorder建構二元樹，可參考[Binary Tree - 演算法筆記](https://web.ntnu.edu.tw/~algo/BinaryTree.html)
- 題目給定兩個數列，分別為一個二元樹的Preorder與Inorder，請以此建構原本的二元樹。

:::success
**Hint**：採用遞迴的寫法，先由Preorder找出root，再將二數列分為兩段，依此建構左右子樹
:::

---

:::info
解題思路 : 
1. ==inorder : LDR 、 preorder : DLR==，所以每次遞迴當中，preorder的第一個都會是root
2. 找到root值後，去找出root在inorder裡的index位置，而在index的左半邊就是左子樹，而index的右半邊則是右子樹
:::
1. 程式碼 : 
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
```
2. 測試結果 :
![](https://i.imgur.com/lLlj2nx.png)
3. 花費時間 : 30 min
4. 自己完成的程度 : 自己想出來

## 5. 由Postorder與Inorder建構二元樹
- [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
- 題目給定兩個數列，分別為一個二元樹的Postorder與Inorder，請以此建構原本的二元樹。

:::success
**Hint**：採用遞迴的寫法，先由Postorder找出root，再將二數列分為兩段，依此建構左右子樹
:::

---

:::info
解題思路 : 
1. ==inorder : LDR 、 postorder : LRD==，所以每次遞迴當中，postorder的最後一個都會是root
2. 找到root值後，去找出root在inorder裡的index位置，而在index的左半邊就是左子樹，而index的右半邊則是右子樹
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        
        last = len(postorder) - 1
        root = TreeNode(postorder[last])
        mid = inorder.index(postorder[last])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:last])
        return root
    
```
2. 測試結果 : 
![](https://i.imgur.com/ghmFfyB.png)
3. 花費時間 : 20 min
4. 自己完成的程度 : 自己想出來


# 本週心得
- 這次反而是觀念題花了我蠻久的時間，最難的莫過於FFT了，一直回放影片看
- 程式題由於上學期資料結構有練習過，所以寫起來蠻輕鬆的，尤其第二題只要把第一題拿來改一下就是答案了
