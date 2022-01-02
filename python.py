with open('qwerty.txt', mode='a') as my_file:
    my_file.write("\nline 4")

with open('qwerty.txt', mode='r') as my_file:
    print(my_file.read())

with open('123.txt', mode = 'w') as f:
    f.write("I CREATED THIS FILE")

with open('123.txt', mode = 'r') as f:
    print(f.read())