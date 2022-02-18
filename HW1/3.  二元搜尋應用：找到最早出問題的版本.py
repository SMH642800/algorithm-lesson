"""
題目：
    已知一個程式，從開發至今有n個版本，但是發現最新的版本是錯的，但可能從更早的版本就開始出錯了，錯誤會一直延續到最新版。題目提供isBadVersion(n)函式，可以測試第n個版本是否有錯，請利用重覆呼叫此函式，找到最早出問題的版本
    278. First Bad Version - LeetCode (https://leetcode.com/problems/first-bad-version/)
ex1:
    若是呼叫isBadVersion(2) = False
    呼叫isBadVersion(3) = False
    呼叫isBadVersion(4) = True
    呼叫isBadVersion(5) = True
    則找到最早出問題的版本為4
ex2:
    若是呼叫isBadVersion(6) = False
    呼叫isBadVersion(7) = False
    呼叫isBadVersion(8) = True
    呼叫isBadVersion(9) = True
    則找到最早出問題的版本為8
"""

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
        