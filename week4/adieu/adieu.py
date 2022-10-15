import inflect


names = []

while True:
    try:
        name = input("String: ").strip()
    except EOFError:
        print()
        break
    else:
        names.append(name)


p = inflect.engine()
mylist = p.join(names)
print(f"Adieu, adieu, to {mylist}")