#RAJI HUMAINAT TIMILEHIN
#FizzBuzz Online Test

for i in range(1,101):      #Creates a loop from 1 to 100 
    if i%3==0 and i%5==0:   #Checkes if the number is a multiple of 3 and 5
        print("FizzBuzz")
    elif i%3==0:            #Checkes if the number is a multiple of 3
        print("Fizz")
    elif i%5==0:            #Checkes if the number is a multiple of 5
        print("Buzz")
    else:
        print(i)
    print("\n")             #print a new line after each number or string
