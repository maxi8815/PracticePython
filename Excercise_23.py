open_file1 = open('/Users/letona/lista1.txt', 'r').read().split()
open_file2 = open('/Users/letona/lista2.txt', 'r').read().split()

new_list = []
for elements in open_file1:
    if elements  in open_file2:
        new_list.append(elements)

print(new_list)