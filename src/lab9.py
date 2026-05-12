def compute_transition_table(needle):
    m = len(needle)
    tf = [{} for _ in range(m + 1)]
    
    if m == 0:
        return tf
    tf[0][needle[0]] = 1
    lps = 0  

    for state in range(1, m + 1):
        for char, next_state in tf[lps].items():
            tf[state][char] = next_state

        if state < m:
            tf[state][needle[state]] = state + 1
            lps = tf[lps].get(needle[state], 0)

    return tf


def find_occurrences(haystack, needle):

    if not needle or not haystack:
        return []

    m = len(needle)
    n = len(haystack)
    tf = compute_transition_table(needle)

    state = 0
    indices = []

    for i in range(n):
        state = tf[state].get(haystack[i], 0)
        
        if state == m:
            indices.append(i - m + 1)

    return indices