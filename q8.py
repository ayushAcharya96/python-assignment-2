'''
8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
'''


def is_prime(number):
  if number < 2:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True


print(is_prime(11))
print(is_prime(21))