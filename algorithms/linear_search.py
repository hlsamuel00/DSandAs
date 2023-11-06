def linear_search(haystack: list[int], needle: int) -> bool:
    for idx in range(len(haystack)):
        if haystack[idx] == needle: return True

    return False