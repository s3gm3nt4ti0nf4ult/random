#!/usr/bin/python
# goo.gl/iPQE89

message = '100000011100010110001111000001000000011100000100001110000001000000000001010000001000000101000100000100000000000001000000000000010100110000111010001011000000100000001000011110000010011000000010100000101000001000000000000010100010000010100110000101000001011000000100110000000100110000011101'

tree = {
'5' : 'yyyyyy',
'6' : 'yyyyyxyy',
'7' : 'yyyyyxyx',
'8' : 'yyyyyxxy',
'9' : 'yyyyyxxx',
'A' : 'yyyyx',
'2' : 'yyyx',
'1' : 'yyxy',
'3' : 'yyxxy',
'B' : 'yyxxxy',
'C' : 'yyxxxx',
'0' : 'yx',
'4' : 'xy',
'D' : 'xxx',
'E' : 'xxyx',
'F' : 'xxyy',
}

def decode(x, y):
    txt = []
    graph = {}
    for k,v in tree.iteritems():
        graph[v.replace('x', x).replace('y', y)] = k
    #print(graph) 
    res = 0
    pos = 0
    while res < len(message)+1:
        if message[pos:res] in graph.keys():
            txt.append(graph[message[pos:res]])
            pos = res
        else:
            res += 1
    print(''.join(txt).strip().decode('hex'))


if __name__ == '__main__':
    decode('1', '0')
