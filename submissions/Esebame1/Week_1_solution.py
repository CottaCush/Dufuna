for a in range (1,100):
  if a%3==0 and a%5==0:
    print('Fizzbuzz\n')
  elif a%3==0:
    print('Fizz\n')
  elif a%5==0:
    print('Buzz\n')
  else:
    print (str(a)+'\n')
