
msg = 1087943696176439095600323762148055792209594928798662843208446383247024


def main():
    for i in range(0, 0xffff):
        try:
            k = msg // i
            n = k.to_bytes((k.bit_length()), 'big')
            print("{} value: {}".format(n.replace(b'\x00', b'').decode('utf=8'), i))
        except:
            pass


if __name__ == '__main__':
    main()
