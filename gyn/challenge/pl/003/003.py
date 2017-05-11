''' Oryginal code:


#!/usr/bin/python
def magic1(a, b): 
  o = 0
  i = 0
  while i < a:  # 1 will be added to 'o' variable a times
    o += 1
    i += 1
  i = 0
  while i < b: # 1 will be added to 'o' variable b times
    o += 1
    i += 1
  return o     # so o = a+b it was incremented one by one.... very long solution, byt try in pypy, should be faster xD


def magic2(a, b):
  o = 0
  i = 0
  while i < b:  # will be done b times
    o = magic1(o, a) # o = o+a 
    i += 1
  return o     # adding 'a', 'b' times makes 'o' equal a*b
n1 = int("2867279575674690971609643216365"
         "4161626212087501848651843132337"
         "3373323997065608342")
n2 = int("1240905467219837578349182398365"
         "3459812983123659128386518235966"
         "4109783723654812937")
n = magic2(magic1(n1, n2), 1337)
print hex(n)[2:-1].decode("hex").splitlines()[0]

Simplifies to:
'''


#!/usr/bin/python
def magic1(a, b):
  return a+b
  
  
def magic2(a, b):
  return a*b
  
  
n1 = int("2867279575674690971609643216365"
         "4161626212087501848651843132337"
         "3373323997065608342")
n2 = int("1240905467219837578349182398365"
         "3459812983123659128386518235966"
         "4109783723654812937")

n = magic2(magic1(n1, n2), 1337)
# print n
print hex(n)[2:-1].decode("hex").splitlines()[0]

# and the password is..... Haslo: "WolneOprogramowanie!"
