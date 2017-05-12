#!/usr/bin/python

from itertools import product
import sys
# assume a <- word b <- word k <- key
# for the fact we know that: a^k^b^k = (a^b)^(k^k) = (a^b)

ciphertext = [
    "1f9111".decode("hex"),
    "1799".decode("hex"),
    "0790001226d8".decode("hex"),
    "0a9e1e5c3ada".decode("hex"),
    "1f".decode("hex"),
    "099e195e".decode("hex"),
    "0a97075a21dac1".decode("hex"),
    "0a9710".decode("hex"),
    "199e075131d3".decode("hex"),
    "1199".decode("hex"),
    "12961350".decode("hex"),
]



def xor(a,b):
    return ''.join([chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(a, b[:len(a)])])


def cracker():
    
    ll = xor('h', ciphertext[6][6]).encode('hex')
    words = open('words.txt', 'r').read().lower().splitlines()
    words6 = [ w for w in words if len(w) == 6]

    midd_xor = xor(ciphertext[2], ciphertext[3])

    for w in product(words6, words6):
        #print(xor(w[0], w[1]), midd_xor)
        if xor(w[0], w[1]) == midd_xor:
            print('Colision found, these words are: w1:{} w2:{}'.format( w[0], w[1]))
            keys = list(set([xor(w[0], ciphertext[2]).encode('hex')+ll,
                    xor(w[0], ciphertext[3]).encode('hex')+ll,
                    xor(w[1], ciphertext[2]).encode('hex')+ll,
                    xor(w[1], ciphertext[3]).encode('hex')+ll])
                    )
                    
            
            for k in keys:
                print('key: {}'.format(k))
                for c in ciphertext:
                    print(xor(k.decode('hex'), c))

            sys.exit(100)

    print('Exhousted')



if __name__ == '__main__':
    cracker()
