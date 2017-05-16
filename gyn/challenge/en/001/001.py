#!/usr/bin/env python
import hashlib
import itertools
import time
target = '76fb930fd0dbc6cba6cf5bd85005a92a'



def main():
    wo = open('dict.txt', 'r').readlines()
    words = {}
    t = time.time()
    for w in wo:
        if len(w.strip()) == 8:
            #words.append(w.strip())
            words[hashlib.md5(w.strip().encode('utf-8')).hexdigest()] = w.strip()


    iterable = iter(itertools.product(words.keys(),words.keys()))
    for i in iterable:
        main_hash = '{:x}'.format(int(i[0],16)^int(i[1],16))#"".join(chr(int(x,16) ^ int(y,16)) for x,y in zip(hash1,hash2))
        #print("{}:{}:{}".format(i[0][0],i[1][0],main_hash))
        if main_hash == target:
            print("Keys FOUND!!! w1:{}, w2={}".format(words[i[0]], words[i[1]]))
            break

    print('Done in {}'.format(time.time()-t))




if __name__ == '__main__':
    main()
