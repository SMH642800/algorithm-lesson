###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW6 
# 概念題 :book: 
## 1.  Minimum Spanning Tree
- 題目 :
    1. 請以Kruskal方法，找出下圖的最小生成樹。請依序列出所選擇加入的邊。
    2. 同上題，請改為使用Prim(從a開始)方法。
    ![](https://i.imgur.com/0a6CGDr.png)

---

- 解答 : 
    1. ![](https://i.imgur.com/9JHDrpn.jpg) 
    2. ![](https://i.imgur.com/i4yiL18.jpg)



## 2. Single Source Shortest Path
- 題目 :
    - 請用Dijkstra演算法找出下圖的由A出發的shortest path tree，並完成右表(共五回合)。
    ![](https://i.imgur.com/3iXV5v3.png)

---

- 解答 : 
    - ![](https://i.imgur.com/oEu7o8v.jpg)
    
## 3. Huffman Code
- 題目 : 
    - 已知一份文件內7個符號出現的頻率為：A:2, B:8: C:3, D:4, E:6, F:10, G:7。
    - 請找出此7個符號的Huffman code。
    - 若有一組編碼為1100110111，求解碼後的符號。

---

- 解答 : 
    1. 
        ![](https://i.imgur.com/IahJBTP.jpg)
    
    2. ==110011011 --> EAG== 


---

# 程式題 : Greedy類型 :desktop_computer:
- 所謂Greedy，就是每回合找最佳解，可得到整體的最佳解
- [更多Greedy類型題目](https://leetcode.com/tag/greedy/)

## 4. 隔出最多的水
- [11. Container With Most Water - LeetCode](https://leetcode.com/problems/container-with-most-water/)
- 題目：
    - 一個水槽有多個等間隔的隔板，任兩個隔板可以擋住一定份量的水。
    - 如下圖所示，由紅色的兩個隔板，所能擋住的水量為兩隔板的間隔乘上較矮隔板高度，7x7=49。
    - 題目會給定一個數列，分別代表隔板的高度。例如下圖就是數列：1,8,6,2,5,4,8,3,7。
    - 請找出由兩個隔板可擋住的最大水量。以下圖為例，就是紅色的兩個隔板，擋入49的水量。
![](https://i.imgur.com/nGRtmdz.png)

---

:::info
解題思路 : 
- 利用left和right指標往中間移動
    - 在移動的過程計算出當下left和right所阻擋出來的面積
    - 跟之前儲存的最大面積進行比較，留下最大值
    - 若left牆的高度和right牆的高度進行比較大小，留下相對最大的
- ==Time Complexity : O(n)，liner solution==
:::
1. 程式碼 : 
``` python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 計算目前能得出的area面積
            now_area = min(height[left], height[right]) * (right - left)
            # 跟之前儲存的max_area進行比較大小，留下最大值
            max_area = max(max_area, now_area)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_area       
```
2. 測試結果 :
![](https://i.imgur.com/26071eq.png)
3. 花費時間 : 25min
4. 自己完成的程度 : 有先看老師給的提示

## 5. 跳到最後-V2
- [45. Jump Game II - LeetCode](https://leetcode.com/problems/jump-game-ii/)
- 題目：
    - 已知一個數列，每個數字代表可以向後跳的最大距離。假設一定可以在跳躍數次後到達最終點。求到達終點的許多跳法中，最少的跳躍次數。
    - 範例1：
    - 輸入：1,1,1,1,1
    - 輸出：4
    - 說明
        - 由index 0的位置，跳躍1個數至index 1。
        - 由index 1的位置，跳躍1個數至index 2。
        - 由index 2的位置，跳躍1個數至index 3。
        - 由index 3的位置，跳躍1個數至index 4。
        - 總共跳了四次。
    - 範例2：
    - 輸入：2,3,1,1,4
    - 輸出：2
    - 說明
        - 由index 0的位置，跳躍1個數至index 1。
        - 由index 1的位置，跳躍3個數至index 4。
        - 總共跳了二次。

---

:::info
解題思路 : 
- 利用left和right指標來圈出目前下一步能走到的index範圍
- 在這範圍裏面，計算出每一個index下一步能走到的最遠距離的index，紀錄最遠值
- 再將left移動至right右邊的index，而right則移動至目前最遠能走到的index
- ==影片解釋 : [Jump Game II - Greedy - Leetcode 45 - Python](https://www.youtube.com/watch?v=dJ7sWiOoK7g)==
:::

1. 程式碼 : 
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = 0  # 設立上一步所有的index，下一步能走到的範圍
        step = 0
        while right < len(nums) - 1:
            far_index = 0  
            for i in range(left, right + 1):
                # 在範圍裡面每一個index能走到最遠的位置
                far_index = max(far_index, i + nums[i])
            # 設定下一個能走到的範圍
            left = right + 1
            right = far_index
            step += 1
        return step
```
2. 測試結果 : 
![](https://i.imgur.com/POSRYqs.png)
3. 花費時間 : 55 min
4. 自己完成的程度 : 上網看解答才懂


# 本週心得
- 程式題第二題真的蠻難的，就算上網找答案，也很多都看不懂為何這樣解，最後好不容易找到一個比較好懂得