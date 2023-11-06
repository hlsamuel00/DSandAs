def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_num = arr[i]
        swap_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                swap_idx = j
        
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i]



if __name__ == '__main__':
    lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(lst)
    selection_sort(lst)
    print(lst)