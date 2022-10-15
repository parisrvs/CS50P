items = {}

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        print()
        break
    else:
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

new_items = sorted(items.keys())
for i in new_items:
    print(f"{items[i]} {i}")



