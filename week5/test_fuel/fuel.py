def main():
    fraction = convert(input("String: "))
    print(gauge(fraction))


def convert(fraction):
    x, y = fraction.strip().split('/')
    if not x.isdigit():
        raise ValueError("X is not an integer.")

    if not y.isdigit():
        raise ValueError("Y is not an integer.")

    if y == '0':
        raise ZeroDivisionError("Can't divide by zero.")

    x = int(x)
    y = int(y)
    f = round((float(x)/float(y))*100.0)

    if f > 100 or f < 0:
        raise ValueError("X > Y")

    return f


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
