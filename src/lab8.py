def solve():
    try:
        with open('ijones.in', 'r') as f:
            lines = f.read().split()
    except FileNotFoundError:
        return

    if not lines:
        return

    W = int(lines[0])
    H = int(lines[1])
    grid = lines[2:2+H]

    dp = [[0] * W for _ in range(H)]
    
    letter_sum = {chr(i): 0 for i in range(97, 123)}

    for row in range(H):
        dp[row][0] = 1
        letter_sum[grid[row][0]] += 1

    for col in range(1, W):
        for row in range(H):
            char = grid[row][col]
            prev_char = grid[row][col-1]

            if char != prev_char:
                dp[row][col] = dp[row][col-1] + letter_sum[char]
            else:
                dp[row][col] = letter_sum[char]

        for row in range(H):
            char = grid[row][col]
            letter_sum[char] += dp[row][col]

    answer = dp[0][W-1]
    if H > 1:
        answer += dp[H-1][W-1] 

    with open('ijones.out', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == "__main__":
    solve()