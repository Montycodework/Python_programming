# Go check wiki to understand prime numbers

number = int(input("Enter the number: "))

def prime_checker(n):
  is_prime = True
  for num in range(2 , number):
    if number % num == 0:
      is_prime = False
  if is_prime:
    print("It is a prime number")
  else:
    print("It is not a prime number")  

prime_checker(number)        

     