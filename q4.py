'''
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first 
item on the list? What is the second item on the list?
'''

friends = ['Suraj', 'Sujan', 'Bibek', 'Ayush', 'Chitiz', 'Pawan']
print(id(friends))
friends.append('Aashish')
print(id(friends))
friends.sort()
print(id(friends))
print(friends[1])