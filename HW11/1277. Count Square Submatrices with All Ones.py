"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

- Example:

  - Input: matrix = 
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]

  - Output: 15

  - Explanation: 
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.
"""


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