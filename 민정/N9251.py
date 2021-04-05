import sys

N1 = ' ' + sys.stdin.readline().rstrip()
N2 = ' ' + sys.stdin.readline().rstrip()

Mat = [[0] * (len(N2)) for _ in range(len(N1))]

for i in range(1, len(N1)):
    for j in range(1, len(N2)):
        if N1[i] == N2[j]:
            Mat[i][j] = Mat[i - 1][j - 1] + 1
        else:
            Mat[i][j] = max(Mat[i - 1][j], Mat[i][j - 1])

print(Mat[-1][-1])