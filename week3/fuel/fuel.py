
while True:
    try:
        x, y = input("fraction: ").strip().split('/')
        x = int(x)
        y = int(y)
        f = round((float(x)/float(y))*100.0)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if f > 100:
            continue
        elif f <= 1:
            print("E")
        elif f >= 99:
            print("F")
        else:
            print(f"{f}%")
        break
