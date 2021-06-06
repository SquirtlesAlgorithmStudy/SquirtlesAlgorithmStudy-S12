def cntans(Basket, Cnt):
  for i in range(len(Basket)-1, 0, -1):
    if Basket[i] == Basket[i-1]:
      Cnt += 1
      del Basket[i-1:i]
      cntans(Basket-2)
    else: return Cnt

def solution(board, moves):
    cnt = 0
    basket = []
    for i in range(len(moves)):
        k = moves[i]-1
        for j in range(4,-1,-1):
            if board[j][k] == 0: continue
            else:
                basket.append(board[j][k])
                board[j][k] = 0
    answer = cntans(basket, cnt)
    print(answer)
#  return answer

arr1 = 	[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

solution(arr1, moves)

#print(solution(arr1, moves))