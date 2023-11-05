def maximos(N, Matrix):
    dp = [[0]*N for _ in range(N)]  # matriz auxiliar

    # c0pia
    for i in range(N):
        dp[N-1][i] = Matrix[N-1][i]

    #  máximo para cada celda 
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = Matrix[i][j] + max(dp[i+1][j], dp[i+1][j+1])
        for j in range(i+1, N):
            dp[i][j] = Matrix[i][j] + max(dp[i+1][j], dp[i+1][j-1])

    # calcular la suma máxima
    max_sum = 0
    for i in range(N):
        max_sum = max(max_sum, dp[0][i])

    return max_sum


print(maximos(2, [[2, 3], [1, 2]]))
