# Enters a loop 100 times
# number denotes the loop count
# the loop starts at one and ends at 100
for number in range (1, 100+1):
    # prints FizzBuzz and ends the loop if number is a multiple of 3 and 5
    if (number % 3 == 0) and (number % 5 == 0):               
        print('FizzBuzz')
        continue

    # prints Fizz if number is a multiple of 3    
    elif number % 3 == 0:
        print('Fizz')

    # prints Buzz if number is a multiple of 5   
    elif number % 5 == 0:
        print('Buzz')

    # prints the number if above statements are not satisfied
    # i.e if number is neither a multiple of 3 and 5 or both
    else:
        print(number) 
