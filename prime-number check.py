
def prime_checker(number):
  is_Prime=True
  for i in range(2, number):
    if number%i==0:
      is_Prime=False

  if is_Prime:
    print(f"Your input {n} is a prime number")
  else:
    print(f"Your input {n} is not a prime number")







n = int(input("Enter the number you want to find prime or not:")) 
prime_checker(number=n)


