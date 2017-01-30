print ("hello world")

for i in range(1,100):
    if (i%15==0):
        print(" Fizzbuzz ",i)
    elif (i%5==0 and i%3!=0):
        print(" Buzz: ",i)
    elif (i%3==0 and i%5!=0):
        print(" Fizz:",i)
    else:
        print(i)
