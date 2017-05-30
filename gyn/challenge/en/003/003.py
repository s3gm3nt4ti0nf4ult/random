#!/usr/bin/env python3
''' Challenge 3 from GynvaelEN Stream'''

import itertools

base_chars = ['0', '1', '2', '3']

data = '''10101011101000110100011101111111011111110111010010110010011100101111001011001001
10111001101000111011111110100101111010011101111011001011001001110101011110110011
11101011111011110111101111011101111111001011001001011001001110110011100101100100
11010001110110011110110100101100100110111001110010111'''.replace('\n', '')

trees = []

def h_trees_generator():
  for i in itertools.permutations(base_chars):
    trees.append([[[i[0], i[1]], i[2]],i[3]])
    trees.append([[i[2], [i[0], i[1]]],i[3]])
    trees.append([i[3],[[i[0], i[1]], i[2]]])
    trees.append([i[3],[i[2], [i[0], i[1]]]])


def h_decode():
  for t in trees:
    m = ""
    print(t)
    pos = 0
    res = 0
    tmp = ''
    while pos < len(data):
      tmp += data[pos]
      pos+=1
      if type(t[int(tmp)]) == str:
        m += t[int(tmp)]
        pos+=1
        tmp = ''
      else:
        pass
      
      print(m)
  

if __name__ == '__main__':
  h_trees_generator()
  h_decode() 
