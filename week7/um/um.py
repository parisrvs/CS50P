import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    c = re.findall(r"(^[u][m]$)|(^[u][m][\W]*)|([\s][u][m][\W]*)", s, flags=re.IGNORECASE)
    d = re.findall(r"[\s]*[u][m][\w]", s)
    return len(c) - len(d)

if __name__ == "__main__":
    main()