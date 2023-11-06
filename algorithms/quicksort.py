from random import randint

def quick_sort(array: list[int]) -> None:
    _quicksort(array, 0, len(array) - 1)


def _quicksort(arr: list[int], low: int, high:int) -> None:
    if low >= high:
        return
    
    pivot_idx = _partition(arr, low, high)

    _quicksort(arr, low, pivot_idx - 1)
    _quicksort(arr, pivot_idx + 1, high)


def _partition(a: list[int], lo: int, hi:int) -> int:
    pivot, idx = a[hi], lo-1
    print(a, pivot)

    for i in range(lo, hi):
        if a[i] <= pivot:
            idx += 1
            a[i], a[idx] = a[idx], a[i]

    idx += 1
    a[hi],a[idx] = a[idx], a[hi]
    return idx


if __name__ == '__main__':
    qs_array = [randint(1,100) for _ in range(randint(5, 50))]
    print(qs_array, len(qs_array))

    quick_sort(qs_array)
    print(qs_array)