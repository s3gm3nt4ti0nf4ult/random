#!/bin/python2

#Kudos&credits to: https://stackoverflow.com/a/1214765/6849518

import struct
from zlib import crc32
import os
pngsig = '\x89PNG\r\n\x1a\n'

def swap_palette(filename):
    with open(filename, 'r+b') as f:
        f.seek(0)
        while True:
            chunkstr = f.read(8)
            if len(chunkstr) != 8:
                break
            length, chtype = struct.unpack('>L4s', chunkstr)
            if chtype == 'PLTE':
                curpos = f.tell()
                paldata = f.read(length)
                paldata = '\x0f\x0f\x0f' + '\xf0\xf0\xf0' + '\x00\xff\xde' + '\xff\x00\xde' + '\xde\xff\x00' + '\x00\x00\x00' + '\xff\xff\xff' + '\xde\xde\xde' 

                f.seek(curpos)
                f.write(paldata)
                f.write(struct.pack('>L', crc32(chtype+paldata)&0xffffffff))
            else:
                f.seek(length+4, os.SEEK_CUR)

if __name__ == '__main__':
    swap_palette('m5_nietajne.png')
