"""
題目：
根號2是1.414…，整數部分是1。根號7是2.645…，整數部分是2。
給定一個n，求開根號後的整數部分
ex1 input 2 , output 1
ex2 input 7 , output 2
ex3 input 9 , output 3
"""

import math
from math import sqrt


def binary_search(num int)
    x = sqrt(num)
    mid = num2.0
    left, right = 0.0, num1.0
    while abs(mid-x)  0.0001
        if midmid  num
            right = mid
            mid = (left+right)2
        else
            left = mid
            mid = (left+right)2
    return int(mid)


def main()
    num = int(input())
    print(binary_search(num))


if __name__ == __main__
    main()
