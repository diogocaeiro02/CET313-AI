def coin_change(coins, amount):
    coins.sort(reverse=True)
    coin_count = 0
    change = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count += 1
            change.append(coin)

    if amount == 0:
        print(f"Minimum number of coins required: {coin_count}")
        print("Coins used:", change)
    else:
        print("Not possible to get the desire change with the coins.")


coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 93

coin_change(coins, amount)
