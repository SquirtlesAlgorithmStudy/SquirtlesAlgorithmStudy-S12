
import sys
input = sys.stdin.readline

def matsum(list1, list2):
  result = [0,0]
  result[0] = list1[0]+list2[0]
  result[1] = list1[1]+list2[1]
  return result

n = int(input())
k = int(input())
result = [[0] * n for _ in range(n) ]
dx = [1, 0]
dx_=[-1,0]
dy = [0, 1]
dy_=[0,-1]
point = [((n+1)//2)-1 , ((n+1)//2)-1]
result[point[0]][point[1]] = 1
save = [0, 0]
j = 1
for i in range(n // 2):

 
 point = matsum(point, dx_) 
 
 for _ in range(2*i +1):
       j+=1
       result[point[0]][point[1]] = j
       if j == k:
         save = point
       point = matsum(point, dy)

 for _ in range(2*i+2):
       j+=1
       result[point[0]][point[1]] = j
       if j == k:
        save = point
       point = matsum(point, dx)
 for _ in range(2*i+2):
       j+=1
       result[point[0]][point[1]] = j
       if j == k:
         save = point
       point = matsum(point, dy_)
 for _ in range(2*i+2):
       j+=1
       result[point[0]][point[1]] = j
       if j == k:
         save = point
       point = matsum(point, dx_)
 j+=1 
 result[point[0]][point[1]] = j    


save[0]+=1
save[1]+=1

for i in range(n):
  print(*result[i])
print(*save)
# 요러한 출력 방식 숙지 !



    
     








