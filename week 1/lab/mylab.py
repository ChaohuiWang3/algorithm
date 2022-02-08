def solution():
    amount = 19
    coins = [1,2,5,10,20,50]
    coins2 = []
    length = len(coins)-1
    for i in range (0,amount+1):
        if amount > coins[length]:
            coins2.append(coins[length])
            amount = amount - coins[length]
        elif amount > 0 and amount < coins[length]:
            for j in range (0,amount+1):
                if amount < coins[length]:
                    length = length - 1
                else:
                    coins2.append(coins[length])
                    break
            amount = amount - coins[length]
        elif amount == coins[length]:
            coins2.append(coins[length])
            print(coins2)
            break
        elif amount == 0:
            print(coins2)
            break
    
solution()
