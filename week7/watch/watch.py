import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s.startswith("<iframe"):
        if matches := re.search(r"https?://(?:www\.)?\w+\.(?:com)/embed/(\w+)", s):
            return f"https://youtu.be/{matches.group(1)}"

    return None


if __name__ == "__main__":
    main()