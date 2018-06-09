for a in range (1,100):
  if a%3==0 and a%5==0:
    print('Fizzbuzz\n')
     continue
  elif a%3==0:
    print('Fizz\n')
     continue
  elif a%5==0:
    print('Buzz\n')
     continue
  print (str(a)+'\n')
