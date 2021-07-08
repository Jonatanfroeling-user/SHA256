from constants import COMP, CONSTS
from basic_operations import *
from helpers.helpers import *
from functions import * 
from time import sleep

# setup: str->bin & padd string to 512 bit string
strA = 'abc'
message = asciiToBin(strA)
blocks = Padd521(message)



# MESSAGE BLOCKS: devide every block in 32bit words (ExtendWord makes sure every word is cocrect size)
block1Words = chunk(blocks[0], 32)
extendedWords = ExtendWord(block1Words)


# COMPRESSION: updates COMP values for each word until all words have been compressed in COMP size
# T1 & T2 are different compression methods that use different 'mutation'functions
def compress(block):
    global COMP
    originalComp = COMP.copy()

    # iterates all compressions [a = 001..01, b = 101..11, c=...]
    for i in range(len(block)):
        Ch = Choice(COMP['e'], COMP['f'], COMP['g'])
        SIG1 = UpperSigma1(COMP['e'])
        h = COMP['h']
        WN = extendedWords[i]
        CN = CONSTS[i]

        # T1 = ∑1(e) + Ch(e, f, g) + h + K0 + W0
        T1 = bin_add(SIG1, Ch, h, WN, CN)

        SIG1_2 = UpperSigma0(COMP['a'])
        Ch_2 = Majority(COMP['a'], COMP['b'], COMP['c'])

        # T2 = ∑1(a) + Ch(a, b, c)
        T2 = bin_add(SIG1_2, Ch_2)
        
        # updates COMP "updateShiftIndex" with new values
        COMP = COMP['updateShiftIndex'](T1, T2)
        
    # removes updateShiftIndex from COMP
    COMP.pop('updateShiftIndex')
    
    # update COMP with addition of original values
    for i in COMP:
        COMP[i] = bin_add(originalComp[i], COMP[i])

compress(extendedWords)  


def concatBinToHex():
    global COMP
    res = ""
    for i in COMP:
        res += hex(int( int(COMP[i], 2)))[2:] 
    return res

pt('result')
print(concatBinToHex())