"""
Given an integer numRows, return the first numRows of Pascal's triangle.

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

"""

# method 1:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)

        return res

======================================================================

# method 2 (more efficiency):

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
