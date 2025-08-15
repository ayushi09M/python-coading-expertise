# Enter a number
n = int(input("Enter a num : "))

# Function to check if number is even or odd
def findNumType(n):
    if(n%2 == 0):
       print("Even Number")
    else:
        print("Odd Number")

# Calling a function
findNumType(n)