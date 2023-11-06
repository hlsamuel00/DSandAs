from random import randint

def merge_sort(array: list) -> None:
    _merge_sort(array, 0, len(array) - 1)

def _merge_sort(arr, lo: int, hi: int) -> None:
    if lo >= hi:
        return 
    
    mid = (lo + (hi - lo) // 2) + 1

    _merge_sort(arr, lo, mid - 1)
    _merge_sort(arr, mid, hi)
    _merge(arr, lo, mid, hi)

def _merge(arr: list, lo: int, mid: int, hi: int) -> None:
    point_1, point_2, current = lo, mid, lo
    copy = arr[:]

    while current <= hi:
        if point_1 < mid and point_2 <= hi:
            if copy[point_1] < copy[point_2]:
                arr[current] = copy[point_1]
                point_1 += 1
            else:
                arr[current] = copy[point_2]
                point_2 += 1
        elif point_1 < mid:
            arr[current] = copy[point_1]
            point_1 += 1
        else:
            arr[current] = copy[point_2]
            point_2 += 1
        
        current += 1


if __name__ == '__main__':
    lst = [randint(1, 100) for _ in range(randint(5, 50))]
    print(lst)

    merge_sort(lst)
    print(lst)