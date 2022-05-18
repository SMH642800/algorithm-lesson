###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW9
# 概念題 :book: 
## 1. 最短路徑
- 題目 : 
    - 請使用Branch-and-Bound找出下圖中，S到T的最短路徑。請畫出Branch-and-Bound圖，並標示各點的cost，以及被bound住的地方。(可參考ppt20頁)
    ![](https://i.imgur.com/FiMgb9j.png)

---

- 解答 : 
    - 先用==hill climb==找出第一組解
        ![](https://i.imgur.com/HfiJOrK.jpg)
        
    - 再由第一組解==限縮擴展的範圍==
        ![](https://i.imgur.com/juwmDjY.jpg)

---

## 2. Personnel Assignment Problem
- 題目 :
   - 已知5個工作(j1,…,j5)，其先後關係為：j1 < j3 , j3 < j4 , j2 < j5，分配給5個人員(p1,…,p5)
    - 其cost matrix如下：
        $\left(\begin{array}{ccc}
                17 & 13 & 4 & 23 & 12 \\
                32 & 30 & 45 & 19 & 31 \\
                7 & 11 & 12 & 3 & 15 \\
                10 & 17 & 13 & 9 & 11 \\
                8 & 19 & 9 & 6 & 7 \\
                \end{array}
        \right)$
    - 例如：p1作j1到j5的工資分別為17,13,4,23,12
    - 每人分配一個工作，且當ja < jb ，須要 pa < pb。
    - 請使用Branch-and-Bound找出最少費用的人員工作分配。

---

- 解答 : 
    - find the ==solution tree== which contains all possible solution : 
        ![](https://i.imgur.com/LJUAbML.jpg)
        
    - then find the ==reduced cost matrix== and ==total least cost==
        - reduced cost matrix : 
            ![](https://i.imgur.com/zsWauhQ.jpg)

        - total least cost : 4+19+3+9+6+1+8+1 = ==51==
    - bounding of subsolutions:
        - 先用==hill climb==找出第一組解
            ![](https://i.imgur.com/KdpXIMe.jpg)

        - 再由第一組解==限縮擴展的範圍==
            ![](https://i.imgur.com/Niwnnzi.jpg)

## 3. Traveling Salesperson Optimization Problem
- 題目 : 
    - 在ppt34頁中，該例首先以4-6將所有feasible solution分為兩集合。
    - 現在，將原例的4-6改以6-7來作區分，接著再以3-5作區分，如下圖所示：
        ![](https://i.imgur.com/EdFYC4Y.png)
    - 請計算出圖中每個紅框的lower bound，並列出reduced matrix。

---

- 解答 : 
    - All solutions **with arc 6-7**:
        - lower bound : ==96==
        - reduced matrix:
            ![](https://i.imgur.com/7rXIEEn.jpg)

    - All solutions **without arc 6-7**:
        - lower bound : 96 + (0+5) = 96 + 5 = ==101==
            ![](https://i.imgur.com/iPaElCY.jpg)

            
    - All solutions **with arc 3-5**:
        - lower bound : ==96==
        - reduced matrix:
            ![](https://i.imgur.com/qgXWDS4.jpg)

    - All solutions **without arc 3-5**:
        - lower bound : 96 + (1+17) = 96 + 18 = ==114==
            ![](https://i.imgur.com/EHJzYgR.jpg)


---

# 程式題 : [Depth-First Search](https://leetcode.com/tag/depth-first-search/) :desktop_computer:


## 4. 左右反轉二元樹
- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- 題目 : 給定一個二元樹，請建立一個左右反轉的二元樹

---

1. 程式碼 : 
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # recursion
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```
2. 測試結果 :
![](https://i.imgur.com/8RhOiZE.png)

3. 花費時間 : 10 min
4. 自己完成的程度 : 自行完成

# 本週心得
- 觀念題的部分，在Traveling Salesperson Optimization Problem當中，課本好像並沒有提到==without arc i-j==的reduced cost matrix要如何做?

---

# 延伸練習:
- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- 題目：給定一個二元搜尋樹，請在其中找出第k小的節點。