"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


- Example:
  - Input: n = 3
  - Output:  ["((()))","(()())","(())()","()(())","()()()"]

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add left paranthesis if left < n
        # only add right paranthesis if right < left
        # valid if left == right == n
        
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