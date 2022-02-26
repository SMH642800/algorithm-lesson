"""
- 題目：
   - 提供一個guess(int n)函式讓你呼叫來猜數字，當
        - 你猜的數字過大時，guess()回傳 -1
        - 你猜的數字過小時，guess()回傳 1
        - 你猜的數字對時，guess()回傳 0
    - 請透過重複呼叫guess()用==最少的次數==來猜到數字。
    - 374. [Guess Number Higher or Lower - LeetCode]
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while True:
            mid = (left+right)//2
            res = guess(mid)
            if res == -1:   # 數字過大，縮限右邊
                right = mid - 1
            elif res == 1:   # 數字過小，縮限左邊
                left = mid + 1
            else:   # 數字剛好，回傳
                return mid