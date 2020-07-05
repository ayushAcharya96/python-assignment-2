'''
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
'''

def find_old_or_young(friends):
  total_age = 0
  total_friends = 0
  friends = list(filter(lambda x: x[2], friends))
  for friend in friends:
    total_age += friend[2]
    total_friends += 1
  average_age = total_age / total_friends
  for friend in friends:
    if friend[2] > average_age:
      print(f'{friend[0]} {friend[1]} : Old')
    else:
      print(f'{friend[0]} {friend[1]} : Young')


friends = [
  ('Aashish', 'Acharya', 20),
  ('Ram', 'Dahal',30),
  ('John', 'Doe', None),
  ('Bruno', 'Fernandes', 24),
  ('Ayush', 'Acharya', 23)
]
find_old_or_young(friends)