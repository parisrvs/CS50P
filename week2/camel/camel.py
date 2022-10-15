name = input("name: ")

new_name = []
j = 0

for i in range(len(name)):
    if name[i].isupper():
        new_name.append((name[j:i]).lower())
        j = i
new_name.append((name[j:i+1]).lower())

if len(new_name) == 1:
    print(new_name[0])
else:
    print('_'.join(new_name))