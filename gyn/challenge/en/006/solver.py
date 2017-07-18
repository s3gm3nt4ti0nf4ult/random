import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageOps


def det_size():
    numbers = []
    with open('data.txt', 'r') as f:
        for l in f.readlines():
            numbers.append(int(l.split(',')[0][1:]))
            numbers.append(int(l.split(',')[1][:-2]))
    return min(numbers)+1, max(numbers)+1


def main():
    x_min, x_max = det_size()
    list_of_points = []
    line = []
    lines = []
    with open('data.txt', 'r') as f:
        for l in f.readlines():
            x, y = (int(l.split(',')[0][1:])),(int(l.split(',')[1][:-2]))
            list_of_points.append((x,y))

    for i in range(x_max):
        line = []
        for j in range(x_max):
            if (j,i) in list_of_points:
                line.append(255)
            else:
                line.append(0)

        lines.append(line)

    y = np.array([np.array(xi) for xi in lines])
    plt.imshow(y,cmap='Greys', interpolation='none')
    name = 'qrdecode.png'
    mir_name = name[:-4]+'_mirr.png'
    plt.axis('off')
    plt.savefig(name)
    #plt.show()
    im = Image.open(name)
    im = ImageOps.mirror(im)
    #im.show()
    im.save(mir_name)


if __name__ == '__main__':
    main()
