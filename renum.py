import sys
import os

file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')

list = []
n = 0
line_number = 0
nb_lines = int(sys.argv[3])
loading = 1

for line in file_in:
    line_number += 1
    (i, j) = line.split('\t', 1)
    i = int(i)
    j = int(j)
    if not (i in list):
        list.append(i)
        k = str(n)
        n += 1
    else:
        k = str(list.index(i))
    if not (j in list):
        list.append(j)
        l = str(n)
        n += 1
    else:
        l = str(list.index(j))
    if loading < (100*line_number)/nb_lines:
        print('Lignes renumerotees : ' + str(loading) + ' pourcents')
        loading += 1
    file_out.write(k + '\t' + l + '\n')