def counting_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)
    counting_arr = [0] * (maxval + 1)

    for v in arr:
        counting_arr[v] += 1

    for i in range(1, maxval + 1):
        counting_arr[i] += counting_arr[i - 1]

    result = [0] * n

    for i in range(n - 1, -1, -1):
        v = arr[i]
        result[counting_arr[v] - 1] = v
        counting_arr[v] -= 1

    return result

def hamster_count(s, c, hamster_list):
    if s < 0 or s > 109:
        raise ValueError("Запас їжі  має бути в межах від 0 до 109") 
    if c < 1 or c > 105:
        raise ValueError("Кількість хом'ячків має бути в межах від 1 до 105")
    
    result = 0
    low = 0
    high = c
    k = 0

    while low <= high:
        k = (high + low)// 2
        if k == 0:
            low = k + 1
            continue
        temp_list = []

        for hamster in hamster_list:
            temp_list.append(hamster[0] + hamster[1] * (k-1))

        sorted_list = counting_sort(temp_list)

        current_sum = 0
        for i in range(k):
            current_sum += sorted_list[i]

        if current_sum <= s:
            result = k
            low = k + 1
        else:
            high = k - 1

    return result
