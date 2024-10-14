name = input("What is your name? ")
other = input("Enter a number to find out if it is prime and whether it is odd or even: ")

try:
    num = int(other)
    isPrime = True
    for i in range(2, int(num ** 0.5 + 1)):
        if num <= 1:
            print(f"{name}: {num} is not a prime number")
        elif num % i == 0:
            isPrime = False
            break
            
    if isPrime == False:
        print(f"{name}: {num} is not a prime number")    
    else:
        print(f"{name}: {num} is a prime number")          
        
    ##checks if the input number is odd or even
    if num  % 2 == 0: 
        print(f"{num} is an even number")
    else: 
        print(f"{num} is an odd number")          
except:
    print(f"{name}: {other} is not an integer")

