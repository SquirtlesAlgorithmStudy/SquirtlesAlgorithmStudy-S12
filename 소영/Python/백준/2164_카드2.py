from collections import deque

num = int(input())
cards = deque([i+1 for i in range(num)]) # 초기화

while(len(cards)!=1):
  cards.popleft()
  a = cards.popleft()
  cards.append(a)

print(cards.pop())
