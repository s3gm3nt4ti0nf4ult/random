#! /usr/bin/env python3


__author__ = 'foxtrot_charlie'
__version__ = '0.1.0a'


import argparse


def main(opts):
	wordlist = open(opts.wordlist, 'r').readlines()
	
	with open(opts.output) as f:
		for w in wordlist:
			w = w.strip()

			if ' ' in w:
				line = w.split(' ')

				if len(line) == 1:
					f.writelines(line)

				elif len(line) == 2:
					candidates = []

					candidates.append(l[0] + l[1])
					candidates.append(l[1] + l[0])
					candidates.append(l[0][0] + l[1])
					candidates.append(l[0][0] + l[1][0])
					candidates.append(l[1] + l[0][0])
					candidates.append(l[1][0] + l[0][0])
					candidates.append(l[0] + l[1][0])
					candidates.append(l[1][0] + l[0])

				else:
					pass



if __name__ == '__main__':
	ap = argparse