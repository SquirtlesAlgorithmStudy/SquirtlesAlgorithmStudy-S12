price = int(input())

change = 1000 - price


coin1 = change // 500
coin2 = (change % 500) // 100
coin3 = (change % 500 % 100) // 50
coin4 = (change % 500 % 100 % 50) //10
coin5 = (change % 500 % 100 % 50 % 10) // 5
coin6 = (change % 500 % 100 % 50 % 10 % 5) // 1

answer = print(coin1 + coin2 + coin3 + coin4 + coin5 + coin6)
