def convert(string):
    string = "🙁".join(string.split(':('))
    string = "🙂".join(string.split(':)'))
    return string


def main():
    print(convert(input()))


main()

