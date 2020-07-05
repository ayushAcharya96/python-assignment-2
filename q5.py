'''
Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
'''

me = ('Ayush', 'Acharya', 23)
people = []
people.append(me)
people.append(('Aashish', 'Acharya', 20))
people.append(('Ram', 'Dahal',30))
people.append(('John', 'Doe', 33))
people.append(('Bruno', 'Fernandes', 24))
print(people)
# Sort by age
people.sort(key=lambda x: x[2])
print("\nSorted by age:", people)
# Sort by first name
people.sort(key=lambda x : x[0])
print("\nSorted by First Name : ", people)
# Sort by last name
people.sort(key=lambda x : x[1])
print("\nSorted by Last Name : ", people)