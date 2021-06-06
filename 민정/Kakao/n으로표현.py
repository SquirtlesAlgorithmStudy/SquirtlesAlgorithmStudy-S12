def solution(N, number):
    answer = -1
    DP = []
    
    for i in range(1,9):
        nums = set()
        nums.add( int(str(N)*i))
        
        for j in range(0,i-1):
            for k in DP[j]:
                for l in DP[-j-1]:
                    nums.add(k+l)
                    nums.add(k-l)
                    nums.add(k*l)
                    if l!=0: nums.add(k//l)
        if number in nums:
            answer = i
            break
        DP.append(nums)
        
    return answer