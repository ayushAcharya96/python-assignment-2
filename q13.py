'''
13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
'''

import csv

def write_in_csv(filename, person_list):
  with open(filename, mode='w') as person_data:
    person_writer = csv.writer(person_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    person_writer.writerow(['name', 'address', 'age'])
    for person in person_list:
      person_writer.writerow(person)

person_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
write_in_csv('q13.csv', person_list)