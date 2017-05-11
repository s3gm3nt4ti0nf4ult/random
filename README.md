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

!!!SPOILER ALERT SPOILER ALERT SPOILER ALERT!!!
And these words are:
[click](gyn/challenge/pl/001/solution)
