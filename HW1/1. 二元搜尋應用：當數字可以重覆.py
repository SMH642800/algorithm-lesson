"""
題目：在排序好的數列中，其中數字有可能重覆，請修改原程式，可以回傳最小的index值
Example 1:
    Input: [1,3,3,6], 3
    Output: 1
    說明：3有在數列中出現兩次，較小的index為1
Example 2:
    Input: [1,3,3,6], 2
    Output: 1
    說明：2沒有在數列中，輸出-1
Example 3:
    Input: [1, 2, 3, 6, 6, 6, 7, 8, 9], 6
    Output: 3
    說明：6在數列中出現3次，最小的index為3
"""


def binary_search(data: list, left: int, right: int, key: int):
    while left <= right:
        mid = (left + right)//2
        if int(data[mid]) < key:
            left = mid + 1
        elif int(data[mid]) > key:
            right = mid - 1
        else:
            # 當第一次找到key的index值時，往前找看看是否還有更小的key的index值
            index_num = binary_search(data, left, mid-1, key)
            if index_num == -1:   # 若沒有更小的index值，則回傳原本第一次的值
                return mid
            else:   # 若有更小的index值，則回傳更小的值
                return index_num
    return -1


def main():
    data = input().split()
    key = int(input())
    left, right = 0, len(data) - 1
    print(binary_search(data, left, right, key))


if __name__ == "__main__":
    main()
