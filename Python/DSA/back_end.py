import string
import unidecode
import random
from sympy import *
import binascii
import hashlib
import base64
import zipfile
import traceback

def Normalize_Data(raw_user_input):        
    final_user_input = unidecode.unidecode(raw_user_input)
    return final_user_input

def Generate_Keys():
    p = randprime(0000000000000,99999999999999)
    q = randprime(0000000000000,99999999999999)
    n = p * q
    fi = (p - 1) * (q - 1)
    e = random.randint(2,fi + 1)
    for _ in iter(int,1):
        if gcd(e,fi) == 1:
            break
        else:
            e += 1

    d = pow(e, -1, fi)
    return p,q,e,n,d

def Get_Hash(path):
    # file = open(path)
    # to_read = file.read()
    # hash_sha3_512 = hashlib.new("sha3_512", to_read.encode("utf-8"))
    # hash_sha3_512 = hash_sha3_512.hexdigest()
    # return hash_sha3_512

    file = open(path,'rb')
    to_read = file.read()
    hash_sha3_512 = hashlib.sha512(to_read).hexdigest()
    return hash_sha3_512
def Save_Data(e,d,n,enc_hash):

    f = open("key.priv","w+")
    e_for_file = base64.b64encode(str(e).encode())
    e_for_file = "RSA " + str(e_for_file)
    f.write(str(e_for_file))

    f = open("key.pub","w+")
    d_for_file = base64.b64encode(str(d).encode())
    d_for_file = "RSA " + str(d_for_file)
    f.write(str(d_for_file))

    f = open("n.key","w+")
    n_for_file = base64.b64encode(str(n).encode())
    n_for_file = "RSA " + str(n_for_file)
    f.write(str(n_for_file))

    for i in range(len(enc_hash)):
        enc_hash[i] = str(enc_hash[i])
    
    enc_hash = " ".join(enc_hash)

    f = open("electronic_sign.sign","w+")
    hash_for_file = base64.b64encode(enc_hash.encode())
    hash_for_file = "RSA_SHA3-512 " + str(hash_for_file)
    f.write(str(hash_for_file))
    f.close()
    
    handle = zipfile.ZipFile('DSA.zip', 'w')
    handle.write('./key.priv', compress_type = zipfile.ZIP_DEFLATED)
    handle.write('./key.pub', compress_type = zipfile.ZIP_DEFLATED)
    handle.write('./n.key', compress_type = zipfile.ZIP_DEFLATED)
    handle.write('./electronic_sign.sign', compress_type = zipfile.ZIP_DEFLATED)
    handle.close()

def Control_Data(enc_hash,base_hash):
    counter = 0;
    for i in range(len(enc_hash)):
        if(i >= len(base_hash)):
            counter += 1
            break;
        if(base_hash[i] != enc_hash[i]):
            counter += 1

    if(counter == 0):
        return True
    if(counter != 0):
        return False

def Decrypt_Base64(epath, npath, dpath, end_data_path):
    e = open(epath).read()
    e = e[6:]
    e = e[:-1]
    dec_e = base64.b64decode(e)
    dec_e = str(dec_e)
    dec_e = dec_e[2:]
    dec_e = dec_e[:-1]
    
    n = open(npath).read()
    n = n[6:]
    n = n[:-1]
    dec_n = base64.b64decode(n)
    dec_n = str(dec_n)
    dec_n = dec_n[2:]
    dec_n = dec_n[:-1]

    d = open(dpath).read()
    d = d[6:]
    d = d[:-1]
    dec_d = base64.b64decode(d)
    dec_d = str(dec_d)
    dec_d = dec_d[2:]
    dec_d = dec_d[:-1]

    enc_data = open(end_data_path).read()
    enc_data = enc_data[15:]
    enc_data = enc_data[:-1]
    dec_data = base64.b64decode(enc_data)
    dec_data = str(dec_data)
    dec_data = dec_data[2:]
    dec_data = dec_data[:-1]

    return dec_e, dec_n, dec_d, dec_data
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
        input[i] = pow(input[i],d,n)
    return input

def Decrypt(input,n,e):
    for i in range(len(input)):
        input[i] = pow(input[i],e,n)

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
                reverse = int(holder,2)
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

def main():
    pass

if __name__=="__main__":
    main()