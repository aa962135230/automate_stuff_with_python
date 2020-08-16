table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]



def print_table(table_data):
      x = len(table_data) 
      y = len(table_data[0]) 

      list_max_length = [] #记录原始矩阵每行中字符串的最大长度

      for m in range(x):
            length = 0
            for n in range(y):
                  if length < len(table_data[m][n]):
                        length = len(table_data[m][n])
            list_max_length.append(length)

      for m in range(y):
            for n in range(x):
                if n == 0:
                    print(table_data[n][m].rjust(list_max_length[n]), end=' ')
                elif n == x-1:
                    print(table_data[n][m].ljust(list_max_length[n]))
                else:
                    print(table_data[n][m].ljust(list_max_length[n]), end=' ')

print_table(table_data)

