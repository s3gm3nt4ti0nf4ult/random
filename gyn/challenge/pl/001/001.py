
import hashlib
import itertools

target = '76fb930fd0dbc6cba6cf5bd85005a92a'



def main():
    wo = open('path\to\wordlist', 'r').readlines()
    words = []
    for w in wo:
        if len(w.strip()) == 8:
            words.append(w.strip())
    wo = []
    iterable = iter(itertools.product(words,words))
    for i in iterable:
        a, b = i[0].strip(), i[1].strip()
        hash1, hash2 = hashlib.md5(a.encode('utf-8')).hexdigest(), hashlib.md5(b.encode('utf-8')).hexdigest()
        main_hash = '{:x}'.format(int(hash1,16)^int(hash2,16))#"".join(chr(int(x,16) ^ int(y,16)) for x,y in zip(hash1,hash2))
        #print("{}:{}:{}".format(a,b,main_hash)) 
        if main_hash == target:
            print("w1:{}, w2={}".format(a,b))
            break




if __name__ == '__main__':
    main()
