'''
10. Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
'''

def convert_string(input_string, seperator):
  temp_string = input_string.lower()
  result_string = temp_string[0]
  for i in range(1,len(temp_string)):
    if temp_string[i] != input_string[i]:
      result_string += seperator
    result_string += temp_string[i]
  return result_string

print(convert_string('ThisIsCamelCase', '_'))
print(convert_string('ThisIsCamelCase', '-'))