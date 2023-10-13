import math

def sum_list(a,b):
   con=0
   for i in range(len(a)):
     a1=max(a)
     b1=max(b)
     con+=abs(a1-b1)
     a.remove(a1)
     b.remove(b1)
   return(con)

a=[4,1,2,5]
b=[5,1,2,4]

sum_list(a,b)

def min_op(N):
    dp = [0] *(N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1]+1
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    return dp[N]

N = 7
min_ops = min_op(N)
print(f"El número mínimo de operaciones es {min_ops}.")
