'''
9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
'''

def binary_search_main(item_list, start_index, end_index, key):
  if start_index <= end_index:
    mid = start_index + (end_index - start_index) // 2
    if item_list[mid] == key:
      return mid
    elif item_list[mid] < key:
      return binary_search_main(item_list, mid+1 , end_index, key)
    else:
      return binary_search_main(item_list, start_index, mid-1, key)
  return -1

def binary_search(item_list, key):
  return binary_search_main(item_list, 0, len(item_list) - 1, key)

print(binary_search([1,3,6,8,9,40,45,46,789,900], 6))
print(binary_search([1,3,6,8,9,40,45,46,789,900], 5))