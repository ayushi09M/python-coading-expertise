##Take input from user
n = int(input("Enter a number: "))

##checking condition for printing statements accordingly
for num in range (1,n):
    if num%3==0 and num%5==0 :
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)