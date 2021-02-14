if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(list(arr))
    # print(arr_set)
    arr = list(arr_set)
    arr.sort()
    print(arr[-2])