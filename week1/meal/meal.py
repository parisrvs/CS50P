def main():
    time = input("Time: ").strip()
    time, format = convert(time)

    if (format and format == "a.m.") and (time == 8 or int(time) == 7):
        print("breakfast time")
    elif format and format == "p.m.":
        if int(time) == 12 or time == 1:
            print("lunch time")
        elif int(time) == 6 or time == 7:
            print("dinner time")
    elif not format:
        if 7 <= time <= 8:
            print("breakfast time")
        elif 12 <= time <= 13:
            print("lunch time")
        elif 18 <= time <= 19:
            print("dinner time")



def convert(time):
    hours, minutes = time.split(':')
    if minutes.endswith("a.m.") or minutes.endswith("p.m."):
        minutes, format = minutes.split(' ')
    else:
        format = False

    hours = float(hours)
    minutes = float(minutes)

    time = hours + (minutes/60)
    return time, format





if __name__ == "__main__":
    main()