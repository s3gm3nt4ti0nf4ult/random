import string

def rot(n, c):
    alfUpper = string.ascii_uppercase
    if c in alfUpper:
        oldIdx = alfUpper.index(c)
        newIdx = (oldIdx + n) % len(alfUpper)
        return alfUpper[newIdx]

def main(msg):
    print("increasing...")
    for i in range(0, len(msg)):
        print(rot(52-i, msg[i]))



if __name__ == '__main__':
    main("KFGS WUSTRX DBZAYE KIGHFL RPNOMS")
