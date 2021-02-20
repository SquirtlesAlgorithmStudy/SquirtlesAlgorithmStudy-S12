import sys
input = sys.stdin.readline

n= int(input().strip())
target = int(input().strip())

matrix = [[0] * n for i in range(n)] 
value = 1 #1~n제곱
direction = 1 #방향
count = 1 #1~n제곱
x= int((n - 1) // 2)
y = int((n - 1) // 2) 
matrix[x][y] = value 
while value != n * n: 
    if (direction == 1): #왼쪽
        for i in range(count): 
            value += 1
            x = x-1 
            matrix[x][y] = value 
            if (value == n*n): 
                break 
        direction = 2 
    elif (direction == 2): #위쪽
        for i in range(count): 
            value += 1 
            y = y+1
            matrix[x][y] = value 
        count += 1 
        direction = 3 
    elif (direction == 3): #오른쪽
        for i in range(count): 
            value += 1 
            x=x+1 
            matrix[x][y] = value 
        direction= 4 
    elif (direction == 4): #아래쪽
        for i in range(count): 
            value += 1 
            y= y-1 
            matrix[x][y] = value 
        count += 1 
        direction = 1 
        
for i in range(n): 
    for j in range(n): 
        print(matrix[i][j], end=" ") 
        if (matrix[i][j] == target): 
            x_location = i+1 
            y_location = j+1
    print() 

print(x_location, y_location)