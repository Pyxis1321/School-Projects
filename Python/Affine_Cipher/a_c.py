import string
import unidecode
from math import gcd

def Key_Control(key_1):
    if gcd(int(key_1),36)  == 1: return 0
    if gcd(int(key_1),36)  != 1: return 1

compare_string = string.ascii_uppercase
compare_string += '0' + '1' + '2' + '3' + '4' + '5' + '6' + '7' + '8' + '9' 

def Normalize_Data(raw_user_input):        
    raw_user_input = raw_user_input.upper()
    unusuall_symbol = string.punctuation
    for i in unusuall_symbol:
        raw_user_input = raw_user_input.replace(i, "")
    final_user_input = unidecode.unidecode(raw_user_input)
    return final_user_input

def Cypher(input, key_1, key_2):
        output = ""
        input = Normalize_Data(input)
        for i in range(len(input)):
            if(input[i] == " "): 
                output += "XSX" 
            else:
                number = (int(key_1) * compare_string.index(input[i]) + int(key_2)) % 36
                output += compare_string[number]
        output = " ".join(output[i:i+5] for i in range(0, len(output), 5))
        return output

def Decypher(input, key_1, key_2):
    output = ""
    input = input.replace(" ", "")
    i = 0
    while (i < len(input)):
        if i > len(input):break
        if(input[i] == "X" and input[i + 1] == "S" and input[i + 2] == "X"):
            i += 3
            output += " "
        else:
            number = ((compare_string.index(input[i]) - int(key_2)) * pow(int(key_1),-1,36)) % 36
            output += compare_string[number]
            i += 1
    return output