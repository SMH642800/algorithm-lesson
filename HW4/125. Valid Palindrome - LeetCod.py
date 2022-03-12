"""
125. Valid Palindrome - LeetCode

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
Example 1:
- Input: s = "A man, a plan, a canal: Panama"
- Output: true
- Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
- Input: s = "race a car"
- Output: false
- Explanation: "raceacar" is not a palindrome.

Example 3:
- Input: s = " "
- Output: true
- Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


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