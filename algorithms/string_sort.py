def string_sort(s: str) -> str:
    sorted_s = ''.join(sorted(s.lower().replace(' ', '')))
    return sorted_s

def string_sort_counts_arr(s: str) -> str:
    alphabet_size = 26
    counts = [0] * alphabet_size

    for char in s:
        if char.isalpha():
            counts[ord(char.lower()) - ord('a')] += 1

    new_str = []

    for idx, num_letter in enumerate(counts):
        new_str.append(chr(idx + ord('a')) * num_letter)

    return ''.join(new_str)

if __name__ == '__main__':
    string = 'The quick brown fox jumps over the lazy dog'
    print(string_sort(string))
    print(string_sort_counts_arr(string))