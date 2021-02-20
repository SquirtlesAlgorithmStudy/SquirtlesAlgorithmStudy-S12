# 작성자 : SH_WON_96
# 2021-02-19
# 알고리즘 - 구현
# 문제번호 : 18406 럭키 스트레이트

# 초기 입력값 받기
import sys
input = sys.stdin.readline

text = "READY"
number = list(map(int,str(input().strip())))

if sum(number[:len(number)//2]) == sum(number[len(number)//2:]):
    text = "LUCKY"
print(text)

