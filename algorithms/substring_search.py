def kmp(string: str, pattern: str) -> int:
    s_len, p_len = len(string), len(pattern)

    if p_len > s_len:
        return -1
    if p_len == s_len:
        return 0 if pattern == string else -1
    if not pattern:
        return 0
    
    lps = _get_lps(pattern)
    i, j = 0, 0
    indices = []

    while i < s_len:
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                indices.append(i - len(pattern))
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return indices if len(indices) > 1 else indices[0] if indices else -1

def _get_lps(s: str) -> list[int]:
    lps = [0] * len(s)
    i, j = 1, 0

    while i < len(s):
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    return lps




def rabin_karp(string: str, pattern: str) -> list[int] | int:
    s_len, p_len = len(string), len(pattern)

    q_mod, a_size, = 101, 256
    hash_s, hash_p = 0, 0
    # hashi = (a_size ** (p_len - 1)) % q_mod

    indices = []
    matched = 0
    
    for i in range(p_len):
        # # complex hash
        # hash_p = (a_size * hash_p + ord(pattern[i])) % q_mod
        # hash_s = (a_size * hash_s + ord(string[i])) % q_mod

        # simple hash
        hash_p = (hash_p + ord(pattern[i])) % q_mod
        hash_s = (hash_s + ord(string[i])) % q_mod
    

    for idx in range(s_len - p_len + 1):
        if hash_s == hash_p:
            matched += 1
            if string[idx: idx + p_len] == pattern:
                indices.append(idx)
            
        if idx < s_len - p_len:
            # # complex hash update
            # hash_s = (a_size * (hash_s - ord(string[idx]) * hashi) + ord(string[idx + p_len])) % q_mod

            # simple hash update
            hash_s = (hash_s - ord(string[idx]) + ord(string[idx + p_len])) % q_mod

    print('total matches: ', matched, 'exact matches: ', len(indices))
    return indices if len(indices) > 1 else indices[0] if indices else -1

        
if __name__ == '__main__':
    s = 'ABCABDABCD'
    pat1 = 'BDA'
    pat2 = 'AB'
    pat3 = 'CDE'

    print(kmp(s, pat1))
    print(kmp(s, pat2))
    print(kmp(s, pat3))
    
    print(rabin_karp(s, pat1))
    print(rabin_karp(s, pat2))
    print(rabin_karp(s, pat3))

    s2 = 'ABABABAABABBAABABA'
    pat4 = 'ABA'
    print(rabin_karp(s2, pat4))

    max()