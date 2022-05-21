###### tags: `演算法導論_課程作業及練習` 
# 演算法作業 HW11
# 概念題 :book: 
## 1. shortest path in multi-stage graph
- 題目 : 
   - 下圖為一個multi-stage graph，請分別以forward approach與backward approach，推導出其最短路徑。 
    ![](https://i.imgur.com/Fu7VSdw.png)

---

- 程式碼:
    ```python
    def forward_shortest_dist(graph):
        global INF
        dist = [0] * N  # dist[i]: 第i點到終點的距離
        dist[N-1] = 0  # 終點設為0

        for i in range(N-2, -1, -1):
            dist[i] = INF
            for j in range(N):   # update dist[i]
                if graph[i][j] == INF:
                    continue
                # 與 i -> j + j -> terminal 的距離進行比較
                dist[i] = min(dist[i], graph[i][j] + dist[j])

        print(dist)
        return dist[0]


    def backward_shortest_dist(graph):
        global INF
        dist = [0] * N  # dist[i]: 來源端到第i點的距離
        dist[0] = 0  # 出發點設為0

        for i in range(1, N):
            dist[i] = INF
            for j in range(N):  # 比對看看，若經過其他點，會不會有較快的路徑
                if graph[j][i] == INF:
                    continue
                # 與 j -> i + star -> j 的距離進行比較
                dist[i] = min(dist[i], graph[j][i] + dist[j])

        print(dist)
        return dist[N-1]


    N = 12
    INF = float("inf")

    # adjacency Matrix
    graph = [[INF, 9, 7, 3, 2, INF, INF, INF, INF, INF, INF, INF],
             [INF, INF, INF, INF, INF, 4, 7, 1, INF, INF, INF, INF],
             [INF, INF, INF, INF, INF, 2, 7, INF, INF, INF, INF, INF],
             [INF, INF, INF, INF, INF, INF, INF, 11, INF, INF, INF, INF],
             [INF, INF, INF, INF, INF, INF, 11, 8, INF, INF, INF, INF],
             [INF, INF, INF, INF, INF, INF, INF, INF, 6, 5, INF, INF],
             [INF, INF, INF, INF, INF, INF, INF, INF, 4, 3, INF, INF],
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, 6, INF],
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4],
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2],
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 6],
             [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]]

    print(forward_shortest_dist(graph))
    print(backward_shortest_dist(graph))
    ```

- 解答 (forward) : 
    ![](https://i.imgur.com/kZEnotO.jpg)

- 解答 (backward) :
    ![](https://i.imgur.com/jzQ6fRd.jpg)


# 程式題 : [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) :desktop_computer:

---

## 2. 計算正方形數量
- [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
- 題目：已知m * n的矩陣，請找出其有多少個1的方陣

---
:::info
- 創建一個dp matrix來儲存資料，然後將matrix的第一列和第一行的資料記錄在dp matrix
- 若dp[i][j]的左、上、左上三個位置都是 >1 ，則在看自己在原本matrix的位置是否等於1
- 若是，代表此位置跟其他三個相鄰的位置能夠形成一個 2*2的方陣
- 若不是，代表此位置無法形成任何一個方陣
:::

1. 程式碼 : 
``` python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
        
        for i in range(n):
            if matrix[0][i] == 1:
                dp[0][i] = 1
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] == 0
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
        
        return ans

```
2. 測試結果 :
![](https://i.imgur.com/2Whd0hn.png)
3. 花費時間 : 20 min
4. 自己完成的程度 : google答案

---

## 3. 所有可能的合法成對括號
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- 題目：給一數字n，請列出所有可能的合法成對括號

---

1. 程式碼 : 
``` python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add left paranthesis if left < n
        # only add right paranthesis if right < left
        # accept if left == right == n
        
        stack = []
        res = []
        
        def backtrack(left, right):
            if left == right == n:
                res.append("".join(stack))
                return
            
            if left < n:
                stack.append("(")
                backtrack(left+1, right)
                stack.pop()
            
            if right < left:
                stack.append(")")
                backtrack(left, right+1)
                stack.pop()
                
        backtrack(0, 0)
        return res
```
2. 測試結果 :
![](https://i.imgur.com/bKabZDa.png)
3. 花費時間 : 40 min
4. 自己完成的程度 : google答案

---

## 4. 巴士卡三角形
- [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
- 題目：給一數字n，請建立一個n層的巴士卡三角形

---

1. 程式碼 : 
    - method 1:
    ``` python
    class Solution:
        def generate(self, numRows: int) -> List[List[int]]:
            if numRows == 1:
                return [[1]]
            if numRows == 2:
                return [[1], [1, 1]]

            ans = []
            for n in range(1, numRows+1):
                temp = [1] * n
                ans.append(temp)

            for i in range(2, numRows):
                for j in range(1, i):
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

            return ans
    ```
    
    - method 2 (more efficiency):
    ``` python
    class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows-1):
            # res[-1]代表res[]的最後一行
            temp = [0] + res[-1] + [0]  
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)

        return res
    ```
    
2. 測試結果 :
![](https://i.imgur.com/UCw2Pzo.png)
3. 花費時間 : 25 min
4. 自己完成的程度 : 自己完成

---

# 本週心得
- 非常喜歡這種上課模式，尤其是寫leetcode的部分，老實說沒有想到老師會加入leetcode解題，因為我哥也是做軟體工程的部分，他時常跟我提起說有空要多刷leetcode的題目，因為大部分的公司基本上都會從leetcode裡面挑題目出來當面試題，因此很高興能夠在上課程的同時順便解leetcode的題目，而且不會的題目也能上網找答案或影片來學習，也很方便。

- 但期中之後的很多題目都是會用到TreeNode的結構，雖然用leetcode的系統寫很方便省事，但期末考用學校的系統，就不曉得該怎麼寫TreeNode結構了，希望不要考太難 (期中考不熟悉學校系統，結果期中考程式都只有部分測資通過而已，若期末也考不及格的話，那就完蛋了)。
