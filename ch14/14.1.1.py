import csv
example_file = open('example.csv')

example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)
print(example_data[1])
print(example_data[0][0])
print(example_data[0][1])
print(example_data[0][2])
print(example_data[1][1])
print(example_data[6][1])