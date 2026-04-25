import math
def prime_checker(number):
     set_prime =True
     if number == 1:
         set_prime = False
     for i in range(2,math.ceil(number/2)):
        if number%i==0:
            set_prime=False
     if set_prime==True:
        print(f"{number} is a Prime no.")
     else:
        print(f"{number} is not a prime no.")
n=int(input("Enter the number :"))
prime_checker(n)