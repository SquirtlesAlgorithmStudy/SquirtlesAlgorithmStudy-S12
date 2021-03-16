# 작성자 : SH_WON_96
# 2021-03-16
# 알고리즘 - Sort
# 문제번호 : 10825 국영수

import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())

# [이름, 국,영,수]
result = []

for _ in range(N):
    name, lan,eng,cal = list(fast_in().strip().split())
    result.append([name,int(lan),int(eng),int(cal)])

# 국어 큰 -> 작, 영 작->큰, 수 큰->작, 영어 알파벳순서(ord순서)
result = sorted(result,key = lambda s: (-s[1],s[2],-s[3], s[0]))

for i in range(N):
    print(result[i][0])

"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""

"""
3
Zoong 50 60 90
coong 50 60 90
Aoong 50 60 90
"""