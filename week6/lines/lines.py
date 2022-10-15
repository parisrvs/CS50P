import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a Python file")


count = 0
try:
    file = open(filename)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    for line in file:
        line = line.strip()
        if line and not line.startswith('#'):
            count += 1
finally:
    file.close()


print(count)


