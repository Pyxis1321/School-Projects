import string
import unidecode
import random
from sympy import *
import binascii

def Normalize_Data(raw_user_input):        
    final_user_input = unidecode.unidecode(raw_user_input)
    return final_user_input

def Generate_Keys():
    p = randprime(0000000000000,99999999999999)
    q = randprime(0000000000000,99999999999999)
    #print('Keys: ',p, q)
    n = p * q
    #print('N: ',n)
    fi = (p - 1) * (q - 1)
    #print('Fi: ',fi)
    e = random.randint(2,fi + 1)
    for _ in iter(int,1):
        if gcd(e,fi) == 1:
            break
        else:
            e += 1
    
    #print('E: ',e)

    d = pow(e, -1, fi)
    #print('D: ',d)

    return p,q,e,n,d

def to_Bin(input):
    my_ascii = []
    for i in range(len(input)):
        my_ascii.append(ord(input[i]))
        
    to_bin = []
    x = 7
    to_bin += [my_ascii[i: i + x] for i in range(0, len(my_ascii), x)]

    for i in range(len(to_bin)):
        for j in range(len(to_bin[i])):
            to_bin[i][j] = format(to_bin[i][j], "08b")

    for i in range(len(to_bin)):
        for j in range(len(to_bin[i])):
            if len(to_bin[i][j]) == 8:
                to_bin[i][j] = '000' + to_bin[i][j] 

    for i in range(len(to_bin)):
        to_bin[i] = ''.join(to_bin[i])
    return to_bin

def Encrypt(input,e,n,d):
    input = Normalize_Data(input)
    input = to_Bin(input)
    for i in range(len(input)):
        input[i] = int(input[i][2:],2)
        input[i] = pow(input[i],e,n)
    return input

def Decrypt(input,n,d):
    for i in range(len(input)):
        input[i] = pow(input[i],d,n)

    output = ''
    actuall_output = ''

    for i in range(len(input)):
        bin_value = format(input[i], "08b")
        reverse_input = bin_value[::-1]
        reverse_input = str(reverse_input)
        j = 0
        itter = 0
        holder = ''
        while j < len(reverse_input):
            holder += reverse_input[j]
            if len(holder) == 8:
                j = j + 4
                holder = holder[::-1]
                #print(holder)
                reverse = int(holder,2)
                #print(reverse)
                output += chr(reverse)
                holder = ''
                continue
            j += 1
        holder = holder[::-1]
        reverse = int(holder,2)
        output += chr(reverse)
        actuall_output += output[::-1]
        output = ''
    return actuall_output

