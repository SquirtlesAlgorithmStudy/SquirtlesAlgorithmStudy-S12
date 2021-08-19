'''
n = 판의수
a = 시작점
b = 목표지점
'''

def hanoi(n,a,b):
    if n==1 :
        print(a,b)
        return
    hanoi(n-1, a, 6-(a+b))
    print(a,b)
    hanoi(n-1 ,6-(a+b) ,b)

n = int(input())
print(2**n-1)

hanoi(n,1,3)
