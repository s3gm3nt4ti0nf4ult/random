import itertools
import string


def check(paswd, ch, e):
    for c in paswd:
        ch = ((ch << 9)&18446744073709551615 | (ch >> 55)&18446744073709551615) ^ ord(c)
    if ch == e:
        return True
    else:
        return False


def brute():
    start_v = int('0x1451723121264133', 16)
    end_v = int('0xc82666f8975a8a05', 16)

    for i in itertools.permutations(string.printable, 5):
        if check(''.join(i), start_v, end_v):
            print("Password is: {}")



if __name__ == '__main__':
    #print(check('GWGW!', int('0x1451723121264133', 16), 14422328074577807877))
    brute()
