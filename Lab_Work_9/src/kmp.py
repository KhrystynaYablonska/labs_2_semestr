def compute_lps(needle: str) -> list[int]:
    """Обчислює масив LPS (Longest Proper Prefix which is also Suffix)."""
    m = len(needle)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(haystack: str, needle: str) -> list[int]:
    """Знаходить індекси всіх входжень підстрічки needle в стрічці haystack
    за допомогою алгоритму Кнутта-Морріса-Прата.
    """
    if not needle or not haystack:
        return []

    n = len(haystack)
    m = len(needle)

    if m > n:
        return []

    lps = compute_lps(needle)
    indices = []
    i = 0  # Індекс для haystack
    j = 0  # Індекс для needle

    while i < n:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices