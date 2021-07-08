from basic_operations import bin_add
from helpers.helpers import *
from helpers.dev import *
from math import floor


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numericals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

CONSTS = {}
COMP = {}

def toBinPadded(nums, pow = 3.0, pattern = False):
    res = {}
    for i in range(len(nums)):
        root = nums[i] ** (1/pow)
        fractional = root - floor(root)
        hexVal = floor(fractional * (2**32))
        paddBin = padd(intToBin(hexVal))
        
        # save as dict
        if pattern:
            res[pattern[i]] = paddBin
        # save as list
        else:
            if isinstance(res, dict):
                res = []
                
            res.append(paddBin)   
    return res


def updateShiftIndex(T1, T2):
    res = {}
    global COMP
    for i in range(len(COMP) - 1):
        l = alphabet[i]
        l2 = alphabet[i - 1]   
        if i == 0:
            res[l] = bin_add(T1, T2)    
        else:
            try:
                res[l] = COMP[l2]
            except:
                continue
    res['e'] = bin_add(res['e'], T1)
    res['updateShiftIndex'] = updateShiftIndex
    COMP = res
    return res


def setupConsts():
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]
    return toBinPadded(nums, 3.0)

        
def setupCompr():
    nums = [2, 3, 5, 7, 11, 13, 17, 19]
    res =  toBinPadded(nums, 2.0, alphabet)
    res['updateShiftIndex'] = updateShiftIndex
    return res
    

# state registers
COMP = setupCompr()
# consts
CONSTS = setupConsts()


    
