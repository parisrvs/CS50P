months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ").strip()
        if valid_format(date):
            break


def valid_format(date):
    if '/' in date:
        try:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            return False
    elif ',' in date:
        try:
            month, day, year = date.split(' ')
            day = int(day.strip(','))
            year = int(year)
            month = month.lower().title()
            month = months.index(month) + 1
        except:
            return False
    else:
        return False

    if (month < 1 or month > 12) or (year < 1 or (day < 1 or day > 31)):
        return False
    else:
        year = str(year)
        day = str(day)
        month = str(month)

    print(f"{year.rjust(4, '0')}-{month.rjust(2, '0')}-{day.rjust(2, '0')}")
    return True


main()




