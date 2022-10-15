string = input("String: ")
vowels = ['a', 'e', 'i', 'o', 'u']
new_string = ''

for i in range(len(string)):
    if string[i].lower() not in vowels:
        new_string = new_string + string[i]

print(new_string)

