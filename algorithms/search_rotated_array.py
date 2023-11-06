def search_rotated_array(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # if we find element, we're done
        if arr[mid] == target:
            return mid
        
        # if arr[low] > arr[mid] -> we have a pivot on the left
        if arr[low] > arr[mid]:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1  
        # if arr[low] < arr[mid] -> we have a pivot on the right or no pivot
        else:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1

def search_rotated_array_with_duplicates(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # if we find element, we're done
        if arr[mid] == target:
            return mid
        
        # if arr[low] == arr[mid], linear search for different value
        while (low != mid and arr[low] == arr[mid]):
            low += 1

        # if arr[low] > arr[mid] -> we have a pivot
        if arr[low] > arr[mid]:
            if arr[mid] <= target <= arr[high]:
                low = mid
            else:
                high = mid - 1

        # if arr[low] < arr[mid] -> we have no pivot, so normal binary search
        else:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    # Test Cases
    arr = [2, 3, 6, 7, 8, 9, 10, 16, 18, 20]
    rotated_arr = [20, 1, 3, 4, 5, 8, 10, 12, 16, 18]

    # for i in range(1, 21):
    #     # idx = i % len(rotated_arr)
    #     # new_rotated_arr = rotated_arr[idx:] + rotated_arr[:idx]
    #     # print(new_rotated_arr)
    #     # print('rotated arr', 'input: ', abs(15 - i), 'output: ', search_rotated_array(new_rotated_arr, abs(15 - i)), '\n')

    for i in range(len(rotated_arr)):
        new_rotated_arr = rotated_arr[i:] + rotated_arr[:i]
        # print(new_rotated_arr)
        # print(search_rotated_array(new_rotated_arr, abs(10 - i)))

        print(search_rotated_array(new_rotated_arr, 4))