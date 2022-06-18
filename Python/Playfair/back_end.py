import string
import unidecode

alphabet = string.ascii_uppercase

def Find_Duplicates(input):
    input = Normalize_Data(input)
    input = input.replace(" ", "")
    uniques = ''
    for char in input:
        if char not in uniques:
            uniques += char
    return uniques

def Fill_Grid(key, langague):
    key = key.upper()
    for i in range(len(alphabet)):
        if alphabet[i] not in key:
            key += alphabet[i]
    if langague == 'EN':
        key = key.replace('J','')
    if langague == 'CZ':
        key = key.replace('Q','')

    grid = []
    x = 5
    grid += [key[i: i + x] for i in range(0, len(key), x)]
    return grid

def Normalize_Data(raw_user_input):        
    raw_user_input = raw_user_input.upper()
    unusuall_symbol = string.punctuation
    for i in unusuall_symbol:
        raw_user_input = raw_user_input.replace(i, "")
    final_user_input = unidecode.unidecode(raw_user_input)
    return final_user_input

def Invalid_Input(input):
    count = 0
    for i in range(len(input)):
        if input[i] == " ":
            count += 1
        if input[i] == '\t':
            count += 1
        if input[i].isdigit():
            count += 1
    if count == len(input): return True
    elif count != len(input): return False

def Invalid_Key(input):
    input = Find_Duplicates(input)
    count = len(input)
    for i in range(len(input)):
        if input[i] == " ":
            count -= 1
        if input[i].isdigit():
            count -= 1
    if count == len(input): return False
    elif count != len(input): return True

def Assign_letter(input,in_a):
    a = ''
    for i in range(in_a, len(input)):
        if in_a + 1 == len(input) and input[i].isdigit():
            a = 0
            a_i = 0
            return a, a_i
        if i + 1 == len(input) and (input[i].isdigit() or input[i] == ' '):
            a = 0
            a_i = 0
            return a, a_i
        if i + 1 == len(input) and input[i] == '\t':
            a = 0
            a_i = 0
            return a, a_i
        if input[i].isalpha():
            a = input[i]
            return a, i

def Get_Pos(a,b,langague,grid):
    ret_a = ''
    ret_b = '' 
    if langague == 'EN':
        if a == 'J':
            a = 'I'
        if b == 'J':
            b = 'I'
    if langague == 'CZ':
        if a == 'Q':
            a = 'K'
        if b == 'Q':
            b = 'K'
    for i in range(5):
        for j in range(5):
            if grid[i][j] == a:
                ret_a += str(i)
                ret_a += str(j)
            if grid[i][j] == b:
                ret_b += str(i)
                ret_b += str(j)
    return ret_a,ret_b

def Output_Grid(grid):
    output = ''
    for i in range(5):
        output += '_' * 15 + '\n'
        for j in range(5):
            output += grid[i][j] + ' | '
        output += '\n'
    return output

def Cipher(input, langague, key):
    key = Find_Duplicates(key)
    grid = Fill_Grid(key,langague)
    input = Normalize_Data(input)
    i = 0
    input = list(input)
    a,b = '',''
    a_i = 0
    b_i = 0
    while i < len(input):
        #Edge casses, not prud of this, sorry to anybody viewing this,
        #didn't have enought time to optimaze due to other asigments
        if input[len(input) - 1] == ' ': input.pop(len(input) - 1)
        if(input[0].isspace() and input[1].isspace() and input[len(input) - 1].isspace()): break
        if i == len(input) - 2 and a_i != 0: break 
        if a_i + 2 == len(input) and input[a_i + 1].isdigit() and input[a_i] != ' ': input.insert(a_i + 1, "X"); break
        if a_i == len(input) - 1 and input[a_i].isdigit(): break
        if a_i == len(input): break      
        if input[a_i] == ' ' and input[a_i + 1].isdigit() and a_i + 2 == len(input): break
        #Searching for first letter
        a,a_i = Assign_letter(input, a_i)

        if a == 0 and a_i == 0: break
        if a_i == len(input) - 1 and a != 'X' and a != ' ': input.insert(a_i + 1, 'X'); break
        elif a_i == len(input) - 1 and a != 'Y': input.insert(a_i + 1, 'Y'); break
        if input[a_i].isdigit and a_i == len(input) - 1: break
        #Searching for second letter
        b,b_i = Assign_letter(input, a_i + 1)

        if b == 0 and b_i == 0: break
        #Getting position of both letters in the grid
        a_pos,b_pos = Get_Pos(a,b,langague,grid)
        #Encoding letters
        if a == b and a_i == b_i - 1 and a != ' ':
            if a != 'X' and b != 'X':
                input[a_i] = a
                input[a_i + 1] = 'X'
                input.insert(int(b_i + 1), b)
                b,b_i = Assign_letter(input, a_i + 1)
                a_pos,b_pos = Get_Pos(a,b,langague,grid)
            elif a != 'Y' and b != 'Y':
                input[a_i] = a
                input[a_i + 1] = 'Y'
                input.insert(int(b_i + 1), b)
                b,b_i = Assign_letter(input, a_i + 1)
                a_pos,b_pos = Get_Pos(a,b,langague,grid)
        if a_pos[0] == b_pos[0]:
            if a_pos[1] == '4':
                input[a_i] = grid[int(a_pos[0])][0]
                input[b_i] = grid[int(b_pos[0])][int(b_pos[1]) + 1]
                i = a_i
            elif b_pos[1] == '4':
                input[a_i] = grid[int(a_pos[0])][int(a_pos[1]) + 1]
                input[b_i] = grid[int(b_pos[0])][0]
                i = a_i
            else:
                input[a_i] = grid[int(a_pos[0])][int(a_pos[1]) + 1]
                input[b_i] = grid[int(b_pos[0])][int(b_pos[1]) + 1]
                i = a_i
            a_i = b_i + 1
        elif a_pos[1] == b_pos[1]:
            if a_pos[0] == '4':
                input[a_i] = grid[0][int(a_pos[1])]
                input[b_i] = grid[int(b_pos[0]) + 1][int(b_pos[1])]
                i = a_i
            elif b_pos[0] == '4':
                input[a_i] = grid[int(a_pos[0]) + 1][int(a_pos[1])]
                input[b_i] = grid[0][int(a_pos[1])]
                i = a_i
            else:
                input[a_i] = grid[int(a_pos[0]) + 1][int(a_pos[1])]
                input[b_i] = grid[int(b_pos[0]) + 1][int(b_pos[1])]
                i = a_i
            a_i = b_i + 1
        else:
            input[a_i] = grid[int(b_pos[0])][int(a_pos[1])]
            input[b_i] = grid[int(a_pos[0])][int(b_pos[1])]
            i = a_i
            a_i = b_i + 1
    input = "".join(input)
    if langague == 'EN': 
        input = input.replace(' ', 'J')
        input = " ".join(input[i:i+5] for i in range(0, len(input), 5))
    if langague == 'CZ': 
        input = input.replace(' ', 'Q')
        input = " ".join(input[i:i+5] for i in range(0, len(input), 5))
    grid_output = Output_Grid(grid)
    return input, grid_output


def Decipher(input, langague, key):
    key = Find_Duplicates(key)
    grid = Fill_Grid(key,langague)
    input = input.replace(' ', '')
    if langague == 'EN':
        input = input.replace('J', ' ')
    if langague == 'CZ':
        input = input.replace('Q', ' ')
    i = 0
    input = list(input)
    a,b = '',''
    a_i = 0
    b_i = 0
    while i < len(input):
        if(input[0].isspace() and input[1].isspace() and input[len(input) - 1].isspace()): break
        if i == len(input) - 2 and a_i != 0: break 
        if a_i == len(input): break
        if a_i + 1 == len(input) and input[a_i] == ' ': break
        if input[a_i] == ' ' and input[a_i + 1].isdigit() and a_i + 2 == len(input): break

        a,a_i = Assign_letter(input, a_i)

        if a == 0 and a_i == 0: break

        if input[len(input) - 1].isdigit() and input[len(input) - 3].isalpha() and input[len(input) - 2] == "X" or input[len(input) - 1] == "Y": break
        if a == False: break

        if a_i == len(input) - 1 and a != 'X': input.insert(a_i + 1, 'X'); break
        elif a_i == len(input) - 1 and a != 'Y': input.insert(a_i + 1, 'Y'); break
        if input[a_i].isdigit and a_i == len(input) - 1: break

        b,b_i = Assign_letter(input, a_i + 1)

        if b == 0 and b_i == 0: break

        a_pos,b_pos = Get_Pos(a,b,langague,grid)

        if a_i == len(input) - 2 and input[a_i + 1] == 'X' or a_i == len(input) - 2 and input[a_i + 1] == 'Y': break
        if a_i == len(input) - 2 and input[a_i + 1].isdigit(): break

        if a_pos[0] == b_pos[0]:
            if a_pos[1] == '0':
                input[a_i] = grid[int(a_pos[0])][4]
                input[b_i] = grid[int(b_pos[0])][int(b_pos[1]) - 1]
                i = a_i
            elif b_pos[1] == '0':
                input[a_i] = grid[int(a_pos[0])][int(a_pos[1]) - 1]
                input[b_i] = grid[int(b_pos[0])][4]
                i = a_i
            else:
                input[a_i] = grid[int(a_pos[0])][int(a_pos[1]) - 1]
                input[b_i] = grid[int(b_pos[0])][int(b_pos[1]) - 1]
                i = a_i
            a_i = b_i + 1
        elif a_pos[1] == b_pos[1]:
            if a[0] == '0':
                input[a_i] = grid[4][int(a_pos[1])]
                input[b_i] = grid[int(b_pos[0]) - 1][int(b_pos[1])]
                i = a_i
            elif b[0] == '4':
                input[a_i] = grid[int(a_pos[0]) - 1][int(a_pos[1])]
                input[b_i] = grid[4][int(a_pos[1])]
                i = a_i
            else:
                input[a_i] = grid[int(a_pos[0]) - 1][int(a_pos[1])]
                input[b_i] = grid[int(b_pos[0]) - 1][int(b_pos[1])]
                i = a_i
            a_i = b_i + 1
        else:
            input[a_i] = grid[int(b_pos[0])][int(a_pos[1])]
            input[b_i] = grid[int(a_pos[0])][int(b_pos[1])]
            i = a_i
            a_i = b_i + 1
    input = "".join(input)
    return input