c = 0
valid_coins = [25, 10, 5]
while c < 50:
    coin = int(input("Coin: "))
    if coin in valid_coins:
        c = c + coin

    if c <= 50:
        print(f"Amount due: {50 - c}")
    else:
        break

if c > 50:
    print(f"Change owed: {c - 50}")