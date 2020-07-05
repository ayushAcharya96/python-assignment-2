'''
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
'''

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a, b):
  return a / b

def is_operator_valid(op):
  if op == '+' or op == '-' or op == '*' or op == '/':
    return True
  return False

while(True):
  input_1 = input('Enter a number : ')
  input_2 = input('Enter a number : ')
  operator = input('Enter operator : ')
  if input_1.isdigit() and input_2.isdigit():
    input_1 = int(input_1)
    input_2 = int(input_2)
    operation_dict = {
      '+': add,
      '-': subtract,
      '*': multiply,
      '/': divide
    }
    if is_operator_valid(operator):
      operation = operation_dict.get(operator)
      try:
        print(f'{input_1} {operator} {input_2} = {operation(input_1,input_2)}')  
      except ZeroDivisionError as error:
        print('Division by zero is not possible.')
    else:
      print('Invalid operator!!!')
  else:
    print('Invalid inputs. Please enter numbers.')
  status = input("Enter 'e' to exit.\nEnter any key to try again.\n")
  if status == 'e' or status == 'E':
    break

