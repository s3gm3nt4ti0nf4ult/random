# Random stuff repo.

Random stuff, short scripts, ctf snippets.


## Gyn

This directory contains solutions of GynvaelColdwind's missions from his streams in both english and polish language.



###### PL: Mission 001

Task was simple, you've been given target hash:

`76fb930fd0dbc6cba6cf5bd85005a92a`

It was produced by xoring two md5 hashes of two english words.

My solution (python):

1. Get eng words list
2. Create dict hash:word
3. Make cartesian product of keys of dict
4. xor each pair of hashes 
5. Compare it with original hash, if it matches... BINGO! 




And these words are:


[click](gyn/challenge/pl/001/solution)


###### PL: Mission 003

Link to task:
[click](http://gynvael.vexillium.org/ext/8849db568879b4549b06c85056ca7e55f04c2229.txt)

Comment: You've been given program that prints you a flag. That's nice, isn't it? Yeah... just wait for the solution. I'm not sooooooo patient... Just read the code. 

My solution:

1. Change magic1 function to return just a+b (in the code I've made some comments if it's not clear for you so far) - nah, not so magic...
2. Change magic2 function to return just a*b - again no magic here.
3. Run your program and.... BINGO!

The password is:


[click](gyn/challenge/pl/003/solution)


