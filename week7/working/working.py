import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"^[1-9][0-2]?(:[0-5][0-9])?\s(AM|PM)\sto\s[1-9][0-2]?(:[0-5][0-9])?\s(PM|AM)$", s):
        return convert_time(s)
    else:
        raise ValueError("Incorrect Format")


def convert_time(s):
    from_time, to_time = s.split(' to ')
    return f"{format_time(from_time)} to {format_time(to_time)}"


def format_time(s):
    t, am_pm = s.split()
    if ':' in t:
        hours, minutes = t.split(':')
    else:
        hours, minutes = t, None

    if am_pm == "PM" and hours != "12":
        hours = str(int(hours) + 12)
    elif am_pm == "AM" and hours == "12":
        hours = "00"


    if len(hours) == 1:
        hours = f"0{hours}"
    if minutes:
        return f"{hours}:{minutes}"
    else:
        return f"{hours}:00"



if __name__ == "__main__":
    main()