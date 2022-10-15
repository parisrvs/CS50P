def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    if not s.isalnum() or (l > 6 or l < 2) or not s[0].isalpha() or not s[1].isalpha():
        return False

    digits = None
    for i in range(2, l):
        if s[i].isdigit():
            digits = s[i:]
            break

    if digits and (digits[0] == '0' or not digits.isdigit()):
        return False

    return True

main()