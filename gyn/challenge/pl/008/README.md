PL: Mission 008

[task](http://gynvael.vexillium.org/ext/70809d8a8c51f6963a882f906dd21c18bd37428b_misja008.txt)

Comment:
This is the thoughest mission so far. Drone crew have done some scanning using LIDAR (some kind of long range laser radar) and under this link:
[click](http://gynvael.coldwind.pl/misja008_drone_io/)
there is an "api" for that drone. As given on that url:
//image here
There is a file. Filename is some kind of a hash (md5 probably). This is a resoult of scanning terrain using LIDAR. In the first line, there is const preamble, that says what version of firmware (my guess) was used. Second line contains co-ordinates of drone during current scan (that is described in that file). During scan drone doesn't move. I next 36 lines, we've got scans of the terrain ahead of the drone. When measurement is done, the drone rotates 10 degrees and scans again. In last four lines, there are files that contains scans after moving to particular direction enum('north','east', 'south','west'). 


My solution:
1. Gynveal has given us some tips, to cache resoults. He also told us, that there is no need to do this task using 'complicated' algorithms (I do not consider BFS or DFS as 'complicated'). The password should be somewhere on the map. 
2. Firstly I've created function python```download()``` to control the flow od downloading data and if there is any need, to redo downloading (in case of something crashes). There is also a function called python```parse()``` which is designed to parse input file and get four files obtained after moving drone to one of the directions (last four lines). I started downloading... After about 20 minutes, my patience was over. I knew, that the area was pretty big, but c'mon! Tons of small little datafiles, creating connections for each of them, downloading every single file... So I decided to do like in this joke about programmer, who has one problem and tries to solve it on threads, I've also started to have more than one problem :D. After parallelization of downloading (Python threading is really cool!), it went much faster. After two and a half of hour, I had all 187812 files downloaded and stored in 'dump' folder. 
3. From this point there ale few ways to go. I've decided to use the simplest and the fastes solution - iterate over all files one by one from that dataset, and plot each scan one by one. To do this I've used: 
python```import numpy as np
	matrix = np.zeros((1500,1500))```
Numpy is realy handy when it comes to matrixes and majority of plotting/image editing libraries supports it. 
To compute co-ordinates of point that was hit by laser and the measurement was conducted there are two simple trigonometrics formulas used:

python```    x = math.floor(math.sin(math.degrees(angle)) * distance)
    y = math.floor(math.cos(math.degrees(angle)) * distance)```

The reason why I'm making `floor()` rounding is that co-ordinates need to be integear. Ofcourse if you have enough memory and horsepower, you can multiply distances and co-ordinates to do all computings on inteager values. `int()` beahves diffrently when it comes to negative numbers. 
So for every point that could be measured by laser, value in matrix was changed from 0 to 255 (from black to white color, as I wanted to obtain wb map).
Technically it is all. Run script using command `python main.py` and wait for your map. 
//progressbar loading gif

4. My first attempt wasn't so sucessful:
//first attempt img
Nither second
//second attempt
[...]
And fourth...
I was trying to manipulate `mult` value, which was a factor used to remove some floating point errors after rounding it to int. That gave me some point of angle:
//four/fifth

Better
//next image

And invert colors:
// next image-white-black

Yeah, that's not the best quality ever seen but... Hack yeah it works! IT REALLY WORKS!!! 

Solver in python:
[solver](link_to_solver)

And the SECRET PASSWORD IS:
[password](link_to_password)

