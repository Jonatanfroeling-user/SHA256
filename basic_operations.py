"""
right shift 32 bits (word)
"""
from helpers.dev import *

# rotation/circular right shift
def rotate(word, n = 32, dir = 'r'):
    if dir == 'r':
        n = n * -1
        
    y = n % len(word)
    return word[y:] + word[:y]


def shift_right(word, n = 32):
    # where do overflown bits go?
    return ''.join(['0' for i in range(n)]) + word[:round(32 - n)]


def shift_left(word, n = 32):
    # where do overflown bits go?
    return  word[n:] + ''.join(['0' for i in range(n)])


def XOR(*bins):
    res = [x for x in bins[0]]
    for bin in bins[1:]:
        for i in range(len(bins[0])):
            res[i] = str(int(res[i]) ^ int(bin[i]))
    return ''.join(res)
        

def XOR_v1(a, b, c = False, returnList = False):
    res = [ str(int(a[i]) ^ int(b[i]) ^  int(c[i]  if c else 0))  for i in range(len(a)) ]
    if returnList:
        return res
    return ''.join(res)


def bin_add(*bin_nums: str, length = 32) -> str:
    res = (bin(sum(int(x, 2) for x in bin_nums))[2:])
    
    res = ''.join(['0' for _ in  range(length - len(res))]) + res
    # while len(res) < length:
    #     res = f"0{res}"
    
    # [-32:] get last 32 bits
    return res[-32:]

