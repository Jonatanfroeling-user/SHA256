def cube(x):
    if 0 <= x: return x ** (1./3.)
    return -( -x) ** (1./3.)

def toHex(b):
    return hex(int(b)).split('x')[1]


def strToBin2(s):
    return ''.join(format(ord(i), '08b') for i in s)


def intToBin(i):
    return "{0:b}".format(int(i))


def asciiToBin(s, joined = True):
    b = [bin(ord(i)) for i in s]
    res = [x[:1] + x[2:] for x in b]
    return ''.join(res) if joined else res

def padd(s, max = 32):
    while len(str(s)) < max:
        s = f"0{s}"
    if len(str(s)) > max:
        s = s[:32]
    return s

def chunk(word, size = 32):
    return [word[i:i + size] for i in range(0, len(word), size)]