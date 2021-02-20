def solution(number, k):
    num_li=[]         
    for i, n in enumerate(number):
        while num_li[-1] < n and k > 0 and len(num_li) > 0:
            num_li.pop()
            k=k-1

        if k==0:
            num_li.append(list(number[i:])
            break
        
        num_li.append(n)

    num_li = num_li[:-k] if k > 0 else num_li
    
    answer = "".join(num_li)
    
    return answer