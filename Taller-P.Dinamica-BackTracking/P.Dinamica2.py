def mindiferencia(arr, n):
    total_sum = sum(arr)
    dp = [[False for i in range(total_sum + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    diff = float('inf')
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            diff = total_sum - 2 * j
            break

    set1, set2 = [], []
    j = total_sum // 2
    for i in range(n, 0, -1):
        if dp[i - 1][j]:
            set1.append(arr[i-1])
        elif j >= arr[i - 1] and dp[i - 1][j - arr[i - 1]]:
            set2.append(arr[i-1])
            j -= arr[i - 1]

    return diff, set1, set2

# ejemplo 
arr = [1, 6, 11,2,10,20,30, 5]
n = len(arr)
diff, set1, set2 = mindiferencia(arr, n)
print("La diferencia mínima es:", diff)
print("El primer conjunto es:", set1)
print("El segundo conjunto es:", set2)
