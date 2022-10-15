from datetime import date, datetime
import sys
import re
import inflect

def main():
    DOB = input("Date of Birth: ")
    if not is_valid(DOB):
        sys.exit("Invalid Format")

    print(f"{get_words(get_minutes(DOB))} minutes")



def get_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return words.capitalize()



def get_minutes(DOB):
    time = date.today()
    format = "%Y-%m-%d"
    dob = datetime.strptime(DOB, format)

    difference = time - dob.date()
    days = difference.days

    return (days * 24 * 60)


def is_valid(DOB):
    if re.match(r"^[0-9]{4}-(([0-1][0-2])|([0][0-9]))-[0-3][0-9]$", DOB):
        return True

    return False





if __name__ == "__main__":
    main()