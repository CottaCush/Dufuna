print ('This is a FizzBuzz Program')
print ('')
number = 1
while number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 ==0:
        print ('Fizz')
    elif number % 5 == 0:
        print ('Buzz')
    else:
        print (number)
    print ('')
    number += 1
