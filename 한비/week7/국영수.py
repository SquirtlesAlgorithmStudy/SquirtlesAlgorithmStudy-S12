
import sys
input = sys.stdin.readline

"""
N = int(input())
grade = []

for _ in range(N):
    grade.append(list(map(str,input().split(" "))))
grade.sort(key=lambda x : str(x[0])) 
grade.sort(key=lambda x:int(x[3]), reverse=True) 
grade.sort(key = lambda x : int(x[2])) 
grade.sort(key = lambda x: int(x[1]), reverse = True)


for i in grade :
    print(i[0])
"""


N = int(input())
grade = []
for _ in range(N) :
    grade.append(list(map(str,input().split(" "))))
    
    grade= sorted(grade,key= lambda x:(-int(x[1]), int(x[2]),-int(x[3]),x[0])) 

for i in grade :
    print(i[0])