###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW10
# 概念題 :book: 
## 1. 0/1背包問題
- 題目 : 
    - 已知有六個物品，其價值和重量如下，背包重量限制為34。
        ![](https://i.imgur.com/tp4YV6d.png)
    - 仿照課本以tree search來解。
    - 請將下圖中的框框中，填入其upper bound與lower bound
        ![](https://i.imgur.com/lXadpgV.png)

---

- 解答 :
 ![](https://i.imgur.com/CwkXRD1.jpg)

:::info
n = 6, M = 34, P(total) = 0
:::
- ![](https://i.imgur.com/pMX4pRO.jpg)
        - Upper bound: - ($P_1$ + $P_2$) = ==-17==
        - Lower bound (**放寬限制**): -[$P_1$ + $P_2$ + 4*( (34-10-19) / 8 ) ] = -19.5 ---> ==-19==

---

:::info
n = 6, M = 34, P(total) = 0
:::
- ![](https://i.imgur.com/xIv9XRf.jpg)
    - Upper bound: $W$=19($W_2$), $P$ =10($P_2$),  P(total) = -7($P_1$) + (-10) = ==-17==
    - Lower bound (**放寬限制**): $W$=19($W_2$)+==5(剩餘可分配空間)==, $P$ =10($P_2$)+4*(5/8),  P(total) = -7($P_1$) + (-12.5) = -19.5 ---> ==-19==
- ![](https://i.imgur.com/YSxuBeg.jpg)
     - Upper bound: $W$=19($W_2$)+8($W_3$), $P$ =10($P_2$)+4($P_3$),  P(total) = 0 + (-14) = ==-14==
    - Lower bound (**放寬限制**): $W$=19($W_2$)+8($W_3$)+==7(剩餘可分配空間)==, P(total) = -[10($P_2$)+4($P_3$)+4*(7/10) ] = -16.8 ---> ==-16==
        

---

:::info
n = 5, M = 34-10=24, P(total) = -7
:::
- ![](https://i.imgur.com/fdbuLuj.jpg)

    - Upper bound: $W$=0, $P$=0,  P(total) = -7($P_1$) + -10($P_2$) = ==-17==
    - Lower bound (**放寬限制**): $W$= ==5(剩餘可分配空間)==, $P$ = 4*(5/8) = 2.5,  P(total) = (-7) + (-10) + (-2.5) = -19.5 ---> ==-19==
    
- ![](https://i.imgur.com/xDPe4II.jpg)

    - Upper bound: $W$=8($W_3$)+10($W_4$), $P$=4($P_3$)+4($P_4$),  P(total) = (-7) + (-8) = ==-15==
    - Lower bound (**放寬限制**): $W$=18+==6(剩餘可分配空間)==, $P$ =4+4+4*(6/12)=10,  P(total) = (-7) + (-10) = ==-17==

---

## 2. A* 解multi-stage shortest path problem
- 題目 :
   - 請使用A* 找出S到T的最短路徑。請畫出樹狀圖，並標示各點的cost，並註明哪裏分枝不用再繼續尋找了
       ![](https://i.imgur.com/Y9tyVa7.png)

---

- 解答 : 
    - ![](https://i.imgur.com/WjC39DF.jpg)
    
    - ![](https://i.imgur.com/clCHOfu.jpg)
    
    - ![](https://i.imgur.com/BzqdxEF.jpg)

    - ![](https://i.imgur.com/zI0FK7L.jpg)

    - ![](https://i.imgur.com/xhrh8IE.jpg)

## 3. Channel Routing Problem
- 題目 : 
    - 請使用A* 解Channel Routing Problem。
    - 本題將原本題目的net 7移除，只剩下7個nets，請找出最少track的安排方式。
        ![](https://i.imgur.com/zmHMzX0.png)

---

- 解答 : ==有誤，須修正==
    - Horizontal(水平) constraint graph (HCG)
        ![](https://i.imgur.com/VsFDGu6.jpg)
        
    - Vertical (垂直) constrain graph (HCG)
        ![](https://i.imgur.com/yjzDb9S.jpg)
        
    - solution tree (A* algorithm) : f(n) = g(n) + h(n) ==第一列的5的h(n)錯誤==
        ![](https://i.imgur.com/YKtjoqQ.jpg)
    
    - track 安排
        ![](https://i.imgur.com/wYUOdIX.jpg)

---

# 程式題 : [Breadth-First Search](https://leetcode.com/tag/breadth-first-search/) :desktop_computer:


## 4. 合併二元樹
- [Merge Two Binary Trees - LeetCode](https://leetcode.com/problems/merge-two-binary-trees/)
- 題目：給定二個二元樹，請建立一個合併兩者的二元樹
- 這題可以用DFS也可用BFS，都可以試試看。

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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        #DFS
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1
```
2. 測試結果 :
![](https://i.imgur.com/cIVUDEF.png)
3. 花費時間 : 25 min
4. 自己完成的程度 : 上網google

---

## 5. 最深葉子的最低共同祖先
- [Lowest Common Ancestor of Deepest Leaves - LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)
- 所謂Lowest Common Ancestor(最低共同祖先)，舉例來說，下圖中xy的最低共同祖先就是深綠色的點。
    - 若當只有一個點時，該點的LCA就是自己。
    - 例如x的最低共同祖先就是x。
    ![](https://i.imgur.com/uwLKvRE.png)
- 題目：給定一個二元樹，找出該二元樹最深的葉子之最低共同祖先
    - 建議以BFS來作。
- 例如下圖中，最深的葉子為7,4,而LCA就是2。
    ![](https://i.imgur.com/Chg4nmt.png)

---
:::info
- 總共會有三種情況:
    - 如果只有根結點，那它本身就是最低的共同祖先節點
    - 如果某兩個最深的child node的深度相同，那麼兩者的共同parent node為最低的共同祖先節點
    - 如果只有一個葉子結點的深度是全樹最深的，那麼該結點為最低的共同祖先節點
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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def getDeepestLeave(root, leave):
            if not root: 
                return None, leave

            left, left_leave = getDeepestLeave(root.left, leave+1)        
            right, right_leave = getDeepestLeave(root.right, leave+1)

            if left_leave == right_leave:
                return root, left_leave
            elif left_leave > right_leave:
                return left, left_leave
            else:
                return right, right_leave
            
        return getDeepestLeave(root, 0)[0]


```
2. 測試結果 :
![](https://i.imgur.com/E2jrho5.png)
3. 花費時間 : 1hr
4. 自己完成的程度 : 上網google，還是有點難理解

---

# 本週心得
- 雖然這次課程影片時間比上次短，但是內容超級非常多，幾乎每處都是細節，每一段都要暫停慢慢理解內容，花費的時間差不多就等於2倍的影片時間了。
- 程式題第二題真的很難寫出來，雖然懂題意，但真的要寫成程式碼時，卻不曉得該怎麼下手，就算上網找答案也看得一知半解。
