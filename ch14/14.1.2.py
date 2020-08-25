import csv

example_file = open('example.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print("ROW #" + str(example_reader.line_num) + ' ' + str(row))