if __name__== '__main__':
    n = input()
    arr = map(int, input().split())
    arr1 = set(arr)
    arr1 = list(arr1)
    m = max(arr1)
    arr1.remove(m)
    print(max(arr1))