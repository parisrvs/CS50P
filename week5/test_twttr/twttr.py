def main():
    string = input("String: ")
    print(shorten(string))


def shorten(word):
    string = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i].lower() not in vowels:
            string = string + word[i]

    return string


if __name__ == "__main__":
    main()