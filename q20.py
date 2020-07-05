'''
20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
'''

def three_sum(numbers):
  result_list = []
  length = len(numbers)
  numbers_dict = {}
  used_index = []
  for index, number in enumerate(numbers):
    numbers_dict[number] = index
  for i in range(length):
    for j in range(i + 1,length):
      target = -(numbers[i] + numbers[j])
      if target in numbers_dict.keys():
        if i not in used_index and j not in used_index and numbers_dict[target] not in used_index:
          a = numbers[i]
          b = numbers[j]
          c = numbers[numbers_dict[target]]
          used_index.append(i)
          used_index.append(j)
          used_index.append(numbers_dict[target])
          result_list.append([a,b,c])
  return result_list


print(three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))
