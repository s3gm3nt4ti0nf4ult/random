# Random stuff repo.

Random stuff, short scripts, ctf snippets.

***
***


## Gyn

This directory contains solutions of GynvaelColdwind's missions from his streams in both english and polish language.

For tasks in polish I will make some comments.


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


***
###### PL: Mission 002

Link to task:


[click](http://gynvael.vexillium.org/ext/cf55a15c2e7c157a8561e9c53b144a6fececc8a2.txt)


Comment: We're given a "matrix" of some weird strings. It looks like valid base64 strings, but after decoding it, agents got only "AAAAAAAAAAAAAAAAAAAAAAAA", this is a result of treating each fragment as separate string. The problem is that it's not valid password. We have to retrive another string from this data. Decoding whole set as single base64 string gives an error. 

My solution:

1. Base64 is ascii compatible, it encodes one of 64 printable character with a value in between (0, 63). Data is divided into chunks of 3 bytes. Number of data bytes should be divisible by 3 (padding if its not).
2. Values in range (0,63) can be presented by 6 bits. 
3. Every 'string' in that matrix starts with 'Q', I retrive 4 LB from every other letter after Q, put them in one byte and then convert it right back to the ASCII.

The password is:

[click](gyn/challange/pl/002/solution)



###### PL: Mission 003

Link to task:

[click](http://gynvael.vexillium.org/ext/8849db568879b4549b06c85056ca7e55f04c2229.txt)

Comment: You've been given program that prints you a flag. That's nice, isn't it? Yeah... just wait for the solution. I'm not sooooooo patient... Just read the code. 

My solution:

1. Change magic1 function to return just a + b (in the code I've made some comments if it's not clear for you so far) - nah, not so magic...
2. Change magic2 function to return just a x b - again no magic here.
3. Run your program and.... BINGO!

The password is:


[click](gyn/challenge/pl/003/solution)

***
