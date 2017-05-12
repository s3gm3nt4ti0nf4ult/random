''' challenge PL 002 '''

data = 'WTTQUdUdXVWeTRUTTUXUTRTQWe'

myDict = {
    'd': 29,
    'e': 30,
    'R': 17,
    'Q': 16,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
}

def password_decode():
    password_bits = []
    password = ""

    for w in data:
        password_bits.append(myDict[w]&0x0F)

    password_bits = zip(*[iter(password_bits)]*2)
    for c in password_bits:
        password += chr((c[0]<<4) + c[1])

    print(password)

if __name__ == '__main__':
    password_decode()
