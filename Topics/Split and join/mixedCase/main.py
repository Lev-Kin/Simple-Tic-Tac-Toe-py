array_str = input().split(" ")
if len(array_str) > 1:
    for i in range(1, len(array_str)):
        array_str[i] = array_str[i].replace(array_str[i][0], array_str[i][0].upper(), 1)

print(''.join(array_str))
