"""
題目：
    給一個排序好的數列，在其中搜尋n，若是找到，則回傳n的index，若無則回傳該插入的位置。
    35. Search Insert Position - LeetCode
Example 1:
    Input: [1,3,5,6], 5
    Output: 2
    說明：5有在數列中，index為2
Example 2:
    Input: [1,3,5,6], 2
    Output: 1
    說明：2沒有在數列中，插入在index為1的位置
"""


def binary_search(data: list, left: int, right: int, key: int):
    curr_num = 0   # 記錄最近一次的index值
    while left <= right:
        mid = (left + right)//2
        if int(data[mid]) < key:
            curr_num = mid + 1
            left = mid + 1
        elif int(data[mid]) > key:
            curr_num = mid
            right = mid - 1
        else:
            return mid
    return curr_num


def main():
    data = input().split()
    key = int(input())
    left, right = 0, len(data) - 1
    print(binary_search(data, left, right, key))


if __name__ == "__main__":
    main()
