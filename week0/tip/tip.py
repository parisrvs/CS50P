def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d, e = d.split('$')
    return float(e)


def percent_to_float(p):
    p, e = p.split('%')
    return (float(p))/100


main()


percent_to_float("15%")