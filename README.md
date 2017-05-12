# Random stuff repo.

Random stuff, short scripts, ctf snippets.

___
## Gyn

This directory contains solutions of GynvaelColdwind's missions from his streams in both english and polish language.

For tasks in polish I will make some comments.


Table of Contents:
      * [Gyn](#gyn)
         * [PL](#pl)
                  * [PL: Mission 001](#pl-mission-001)
                  * [PL: Mission 002](#pl-mission-002)
                  * [PL: Mission 003](#pl-mission-003)
         * [EN](#en)
                  * [EN: Mission 001](#en-mission-001)
***
### PL
###### PL: Mission 001

Link to task:


[click](https://youtu.be/fBEe8DGZL5o?t=5416)


We've been given ciphertext, encrypted with XOR (which is not encryption... and by any means should not be used as one - to read: one time pad), there is also some information about key. It's 160 bits long. That's all. How to decrypt message?

`ciphertext:
1f9111
1799
0790001226d8
0a9e1e5c3ada
1f
099e195e
0a97075a21dac1
0a9710
199e075131d3
1199
12961350
`

My solution:
1. Given sample (or ciphertext) is not long. Creating histograms and trying frequency analisys is not the way to go here.
2. So how about xor operation itself. As we know `x ^ x = 0`. So if ciphertext is created in a way: `c = a^k` where c is a ciphertext, a is text message to be encrypted and k is a key, we can xor two strings from ciphertext encrypted with the same key. ` a^k^b^k = (a^b)^(k^k) and k^k = 0, so a^k^b^k = a^b`. And what are these a and b? Well, english words!
3. Let's grab long enough (6 chars long) words, xor them and check if they match xored sample strings. PWNED! 
4. The longest word has 7 characters, but there is only one such word, so I decided to use 6 chars long strings from sample. 
7. After finding 'collision', a pair of words described in `2.`, we've got pretty much all. Only one char is missing, but we can guess it from  the context. Well done!


And the soultion is:


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

[click](gyn/challenge/pl/002/solution)


***
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
***
### EN
###### EN: Mission 001

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


[click](gyn/challenge/en/003/solution)


***
