def rabin_karp(text, pattern):
    m = len(pattern)

    p_hash = hash(pattern)

    for i in range(len(text) - m + 1):
        sub = text[i:i+m]
        if hash(sub) == p_hash:
            if sub == pattern:
                print("Found at index", i)


# Example
rabin_karp("ABCCDDAEFG", "CDD")