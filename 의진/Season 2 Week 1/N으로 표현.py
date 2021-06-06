def operation(a, b, dp, dp_, index):
    if b == 0 : dp[index].append(dp_[index])
    else:
     for value in a:
            dp[index].append(value + b)
            dp[index].append(value - b)
            dp[index].append(b - value)
            dp[index].append(value * b)
            dp[index].append(value // b)
            if value !=0 : dp[index].append(b // value)



def solution(N, number):
    dp_= [0,N]
    for i in range(2,9):
        dp_.append(N * (10 ** (i-1))+ dp_[i-1])
    dp = [[] for _ in range(9)]
    dp[1].append(N)

    for i in range(2, 9):
        for j in range(1, i+1):
            operation(dp[j],dp_[i-j],dp,dp_, i)
    
    
    for i in range(1, 9):
        for j in range(len(dp[i])):
            if dp[i][j] == number : return i
    return -1