from basic_operations import * 
from helpers.helpers import *


def Sigma0(word):
    rorA = rotate(word, 7)
    rorB = rotate(word, 18)
    shrA = shift_right(word, 3)
    xorA = XOR(rorA, rorB)
    return XOR(xorA, shrA)


def Sigma1(word):
    rorA = rotate(word, 17)
    rorB = rotate(word, 19)
    shrA = shift_right(word, 10)
    xorA = XOR(rorA, rorB)
    res = XOR(xorA, shrA)
    return res


def UpperSigma0(word):
    rorA = rotate(word, 2)
    rorB = rotate(word, 13)
    rorC = rotate(word, 22)
    xorA = XOR(rorA, rorB)
    res = XOR(xorA, rorC)
    return res


def UpperSigma1(word):
    rorA = rotate(word, 6)
    rorB = rotate(word, 11)
    rorC = rotate(word, 25)
    xorA = XOR(rorA, rorB)
    res = XOR(xorA, rorC)
    return res


def Choice(a, b, c):
    return ''.join([b[i] if a[i] == '1' else c[i] for i in range(len(a))])
    
    
def Majority(a, b, c):
    return ''.join(['0' if int(a[i]) + int(b[i]) + int(c[i]) < 2 else '1' for i in range(len(a))])

    
    
def Padd521(bytes):
    res = []
    messageBlocks = chunk(bytes, 512)
    
    def checkLen(c):
        return True if len(c) == 512 else False
    
    for block in messageBlocks:
        messageLength = intToBin(len(block))
        paddedMessage = ""


        if checkLen(block):
            return block
        
        block += '1'
        if checkLen(block):
            return block
        
        while len(block) < 448:
            block += '0'
        
        while len(paddedMessage) < (64 - len(messageLength)):
            paddedMessage += '0'
        paddedMessage += messageLength
        block += paddedMessage
        res.append(block)
        
    return res
    
def ExtendWord(words):
    while len(words) < 64:
        l = len(words)
        words.append(bin_add( Sigma1(words[l - 2]), words[l - 7], Sigma0(words[l - 15]), words[l - 16] ))
    return words
