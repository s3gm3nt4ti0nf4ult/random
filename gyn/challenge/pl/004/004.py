#!/bin/python3


def check(paswd):
    
    ch = 0x1451723121264133
    e = 0xc82666f8975a8a05

    for c in paswd:
        ch = ((ch << 9)&18446744073709551615 | (ch >> 55)&18446744073709551615) ^ ord(c)
    if ch == e:
        return True
    else:
        return False


def crack():
    end_v = 0x1451723121264133
    start_v = 0xc82666f8975a8a05

    slicer = 18446744073709551615
    

    tmp = end_v
    password = ""

    end_v <<= 45

    end_v &= slicer

    for i in range(5):
        password = chr((end_v ^ start_v)&0xff) + password
        end_v >>= 9
        end_v &= slicer
        start_v >>=9 
        start_v &= slicer


    print(check(password))
    print(password)




if __name__ == '__main__':
    crack()
