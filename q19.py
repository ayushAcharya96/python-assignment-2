'''
19. Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
'''


OPEN_PARENTHESIS = ['[','{','(']
CLOSE_PARENTHESIS = [']','}',')']

def is_valid(parentheses_list):
  stack = []
  for parenthesis in parentheses_list:
    if parenthesis in OPEN_PARENTHESIS:
      stack.append(parenthesis)
    elif parenthesis in CLOSE_PARENTHESIS:
      index = CLOSE_PARENTHESIS.index(parenthesis)
      if len(stack) > 0 and (OPEN_PARENTHESIS[index] == stack[len(stack) - 1]):
        stack.pop()
      else:
        return "Invalid"
  if len(stack) == 0:
    return "Valid"
  else:
    return "Invalid"

print(is_valid('[]{}()'))
print(is_valid('[[{}(){()()}]]'))
print(is_valid('[[][{]'))