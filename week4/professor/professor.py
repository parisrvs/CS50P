import random


def main():
    level = get_level()
    count = 0
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        while count < 3:
            try:
                result = int(input(f"{x} + {y} = "))
            except ValueError:
                count += 1
                print("EEE")
            else:
                if x + y == result:
                    count = 0
                    score += 1
                    break
                else:
                    count += 1
                    print("EEE")

        if count:
            print(f"Correct Amswer: {x} + {y} = {x+y}")
            count = 0

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level [1, 2, or 3]: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level



def generate_integer(level):
    ulimit = ((10**level)-1)
    if level == 1:
        llimit = ((10**(level-1))) - 1
    else:
        llimit = ((10**(level-1)))

    return random.randint(llimit, ulimit)


if __name__ == "__main__":
    main()