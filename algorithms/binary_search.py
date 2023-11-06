def binary_search(haystack: list[int], needle: int) -> bool:
    low, high = 0, len(haystack)

    while low < high:
        mid = low + (high - low) // 2
        if haystack[mid] == needle:
            return True
        elif haystack[mid] > needle:
            high = mid
        else:
            low = mid + 1
    
    return False