#!/bin/python3

msg = ''' E0 81 8F 76 65 72 C1 AC E0 81 AF E0 81 AE C1 A7
          E0 80 A0 E0 81 95 C1 94 E0 81 86 2D E0 80 B8 E0
          80 A0 F0 80 81 B7 C1 A1 73 20 C1 B3 F0 80 81 B5
          63 C1 A8 20 E0 81 A1 F0 80 80 A0 E0 81 A6 F0 80
          81 B5 F0 80 81 AE 20 E0 81 A6 E0 81 A5 F0 80 81
          A1 C1 B4 75 E0 81 B2 E0 81 A5 F0 80 80 AE'''.replace('\n', '').split()
         
         
def main():
  enc = [bin(int(n, 16))[2:] for n in msg]
  print([len(l) for l in enc])
  
  
if __name__ == '__main__':
  main()