number = int(input())
if number != 1:
    for n in range(2, number):
        if number % n == 0:
            print('This number is not prime')
            break
    else:
        print('This number is prime')
else:
    print('This number is not prime')
