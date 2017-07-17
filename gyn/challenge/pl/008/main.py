import urllib.request
import os
from threading import *
import sys
import itertools
import time
import numpy as np
from PIL import Image
import math
import progressbar
import PIL.ImageOps    



cache = {}
done = False
addr = 'http://gynvael.coldwind.pl/misja008_drone_io/scans/'
l = Lock()
directory = 'dump/'
sign = ['|','/','-','\\']
dots = ['.', '..', '...']
pybar = progressbar.ProgressBar()


def download(filename):
    if os.path.isfile(directory + filename):
        print('We are just lucky! Directory HIT! File {} is in directory!'.format(filename))
        return True
    try:
        url = addr + filename
        print('DOWNLOADING {}'.format(filename))
        urllib.request.urlretrieve(url, directory + filename)
    except:
        print('Cannot download {} will try later'.format(filename))
        return False
    l.acquire()
    cache[filename] = 'NO'
    l.release()
    return True


def download_thread(fn):
    while True:
        if download(fn) is True:
            break


threads = []


def parse(filename):
    filename = filename.strip()
    path_name = directory + filename
    try:
        with open(path_name, 'r') as f:
            pass
    except FileNotFoundError:
        download(filename)

    with open(path_name, 'r') as f:
        print('Parsing: {} '.format(filename))
        lines = f.readlines()[-4:]

        for l in lines:
            fn = l.split(':')[-1].strip()
            if fn not in cache.keys() and fn != 'not possible':
                print('Got {}, which is not in cache, Will download'.format(fn.strip()))
                thread = Thread(target=download_thread, args=[fn])
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()


def find_key():
    for key, value in cache.items():
        if value == 'NO':
            return key
        else:
            pass


def loading_animation(message, wait_symbol):
    for c in itertools.cycle(wait_symbol):
        if done:
            break
        sys.stdout.write('\r' + message + ' ' + c)
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\rDone!')


def compute_cords(angle, distance):
    x = math.floor(math.sin(math.degrees(angle)) * distance)
    y = math.floor(math.cos(math.degrees(angle)) * distance)
    return x, y


def process_data():
    matrix = np.zeros((15500, 15500), dtype=np.int8)
	
    mult = 15
    for file in pybar(os.listdir(directory)):
        filename = directory + file
        with open(filename, 'r') as f:
            lines = f.readlines()
            lines = lines[1:]
            lines = lines[:-4]
            d_x, d_y = (int(lines[0].split(' ')[0]) * mult, int(lines[0].split(' ')[1]) * mult)
            # print('d_x = {} \t d_y = {}'.format(d_x, d_y))
            # matrix[d_x, d_y] = 2
            for i in range(1, len(lines)-1):
                distance = float(lines[i].strip()) * mult
                if distance == float('inf'):
                    continue
                else:
                    x, y = compute_cords(i*10, distance)
                    matrix[d_y-y][d_x+x] = 255
	
    im = Image.fromarray(matrix).convert('RGB')
    im.save('map.bmp')
    im =  PIL.ImageOps.invert(im)
    im.save('map_inverted.bmp')


def main():
    global cache
    '''
    print('Checking if directory exists')
    if not os.path.exists(directory):
        print('Creating directory')
        os.makedirs(directory)
    global done
    t = Thread(target=loading_animation, args=['Looking for files', dots])
    t.start()
    cache = {f: 'NO' for f in os.listdir(directory) if os.path.isfile(directory + f)}
    done = True
    t.join()

    print('Checking...')
    if len(os.listdir(directory)) == 187812:
        print('All files downloaded!')
        done = False
        t = Thread(target=loading_animation, args=['Building cache... ', sign])
        t.start()
        for c in cache.keys():
            cache[c] = 'YES'
        done = True
        t.join()

    while 'NO' in cache.values():
        print('Another iteration! Cached: {}'.format(len(cache)))
        file = find_key()
        if file is not None:
            parse(file)
            cache[file] = 'YES'

    print('DOWNLOADED ALL DATA! PROCESSING')
    print('Clearing cache...')
    cache = {}
    '''
    process_data()


if __name__ == '__main__':
    main()
