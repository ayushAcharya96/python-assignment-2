'''
6. Create a list with names of friends and collegues. Search
 for the name 'John' using a loop. Print ;not found; if you 
 didn't find it.
'''

def find_friend(friend_list, friend):
  result = 'Not found'
  for f in friend_list:
    if f.lower() == friend.lower():
      result = 'Found'
      break
  return result

friends = ['Suraj', 'Sujan', 'John', 'Bibek', 'Ayush', 'Chitiz', 'Pawan']
print(find_friend(friends, 'John'))