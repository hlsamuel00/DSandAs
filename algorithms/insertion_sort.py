def insertion_sort(arr: list) -> list:
    swaps = 0
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swaps += 1
            else:
                break
    return swaps

if __name__ == '__main___':
    lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(lst)
    print(insertion_sort(lst))
    print(lst)
