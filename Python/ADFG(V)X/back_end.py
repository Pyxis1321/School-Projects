import string
import unidecode
import random

def Normalize_Data(raw_user_input):        
    raw_user_input = raw_user_input.upper()
    unusuall_symbol = string.punctuation
    for i in unusuall_symbol:
        raw_user_input = raw_user_input.replace(i, '')
    final_user_input = unidecode.unidecode(raw_user_input)
    return final_user_input

def Check_Key_Length(ot,key):
    if len(key) <= len(ot) * 2: return False
    else: return True

def Normalize_key(key):
    key = key.upper()
    unusuall_symbol = string.punctuation + ' '
    for i in unusuall_symbol:
        key = key.replace(i, '')
    ret_key = unidecode.unidecode(key)
    return ret_key

def Invalid_Key(input):
    count = len(input)
    if len(input) == 0: return True
    for i in range(len(input)):
        if input[i] == " ":
            count -= 1
        if input[i].isdigit():
            count -= 1
    if count == len(input): return False
    elif count != len(input): return True

def Check_Grid(grid,size):
    grid = Normalize_Data(grid)
    grid = grid.replace(" ", "")
    uniques = []
    duplicates = []
    for letter in grid:
        if letter in uniques:
            duplicates += letter
        if letter not in uniques:
            uniques += letter
        if letter.isdigit() and size == '5x5':
            return 2,grid
        if size == '5x5' and len(grid) != 25:
            return 3,grid
        if size == '6x6' and len(grid) != 36:
            return 4,grid
        if len(grid) == 0: return 5
    if len(duplicates) > 0 : return 1, grid
    else: return 0,grid

def Fill_Grid(langague, size, mode, input):
    grid = []
    if mode == 'auto':
        alphabet = string.ascii_uppercase 
        if size == '5x5':
            if langague == 'EN':
                alphabet = alphabet.replace('J', '')
            if langague == 'CZ':
                alphabet = alphabet.replace('Q', '')

        if size == '5x5':
            alphabet = ''.join(random.sample(alphabet,len(alphabet)))
            x = 5
            grid += [alphabet[i: i + x] for i in range(0, len(alphabet), x)]
            return grid

        if size == '6x6':
            alphabet += string.digits
            alphabet = ''.join(random.sample(alphabet,len(alphabet)))
            x = 6
            grid += [alphabet[i: i + x] for i in range(0, len(alphabet), x)]
            return grid
    if mode == 'man':
        if size == '5x5':
            alphabet = input
            x = 5
            grid += [alphabet[i: i + x] for i in range(0, len(alphabet), x)]
            return grid
        if size == '6x6':
            alphabet = input
            x = 6
            grid += [alphabet[i: i + x] for i in range(0, len(alphabet), x)]
            return grid

def Print_Grid(grid,size,mod):
    output = ''
    if size == '5x5' and mod == 'man':
        z = 0
        while z < 25:
            if z == 0: 
                output += '| ' + grid[z] + ' | '
                z += 1
            if z % 5 == 0:
                output += '\n' + '_' * 15 + '\n'
                output += '| ' + grid[z] + ' | ' 
                z += 1
            if z % 5 != 0:
                output += grid[z] + ' | '
                z += 1
                continue
        return output
    if size == '5x5' and mod == 'auto':
        for i in range(5):
            if i != 0:
                output += '_' * 15 + '\n'
            for j in range(5):
                if j == 0: output += '| '
                output += grid[i][j] + ' | '
            output += '\n'
        return output
    if size == '6x6' and mod == 'auto':
        for i in range(6):
            if i != 0:
                output += '_' * 15 + '\n'
            for j in range(6):
                if j == 0: output += '| '
                output += grid[i][j] + ' | '
            output += '\n'
        return output
    if size == '6x6' and mod == 'man':
        z = 0
        while z < 36:
            if z == 0: 
                output += '| ' + grid[z] + ' | '
                z += 1
            if z % 6 == 0:
                output += '\n' + '_' * 15 + '\n'
                output += '| ' + grid[z] + ' | ' 
                z += 1
            if z % 6 != 0:
                output += grid[z] + ' | '
                z += 1
                continue
        return output

def Get_Pos(a,langague,grid):
    ret_a = ''
    if len(grid) == 5:
        if langague == 'EN':
            if a == 'J':
                a = 'I'
        if langague == 'CZ':
            if a == 'Q':
                a = 'K'
    
    if a.isdigit() and len(grid) == 5: return a
    if a == ' ': return a
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == a:
                ret_a += str(i)
                ret_a += str(j)
    return ret_a

def Substitution(OT,langague,grid):
    OT = Normalize_Data(OT)
    output = []
    i = 0
    while i < len(OT):
        a = Get_Pos(OT[i], langague, grid)
        if(len(grid) == 5):
            if OT[i].isdigit() or a == ' ':
                output.append(a)
                i += 1
                continue
            match a[0]:
                case '0': output.append('A')
                case '1': output.append('D')
                case '2': output.append('F')
                case '3': output.append('G')
                case '4': output.append('X')
            match a[1]:
                case '0': output.append('A')
                case '1': output.append('D')
                case '2': output.append('F')
                case '3': output.append('G')
                case '4': output.append('X')
            i += 1
        if(len(grid) == 6):
            if a == ' ':
                output.append(a)
                i += 1
                continue
            match a[0]:
                case '0': output.append('A')
                case '1': output.append('D')
                case '2': output.append('F')
                case '3': output.append('G')
                case '4': output.append('V')
                case '5': output.append('X')
            match a[1]:
                case '0': output.append('A')
                case '1': output.append('D')
                case '2': output.append('F')
                case '3': output.append('G')
                case '4': output.append('V')
                case '5': output.append('X')
            i += 1
    output = "".join(output)
    return output

def Prep_Transposition(input, key):
    key = Normalize_key(key)
    grid = []
    x = len(key)
  
    input = input.replace(' ', '_')
    grid += [input[i: i + x] for i in range(0, len(input), x)]

    unsorted_key = key
    unsorted_key = list(unsorted_key.strip(""))
    key = sorted(key)

    key_index = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i] == unsorted_key[j]:
                key_index.append(j)
                unsorted_key[j] = ' '

    len_last_list = len(grid[len(grid) -1])
    lengths = []

    for i in range(len(grid[0])):
        if len_last_list != 0:
            lengths.append(len(grid) + 1)
            len_last_list -= 1
        else:
            lengths.append(len(grid))

    return grid, key, key_index, lengths

def Transpose(input, key):
    key = Normalize_key(key)
    input,key,key_index,lengths = Prep_Transposition(input, key)

    output = []
    for i in range(len(key)):
        column = key_index[i]
        if column < len(lengths) + 1:
            for j in range(lengths[column]):
                if j == lengths[column] - 1 and i <= len(key): 
                    output.append(' ')
                    continue
                output.append(input[j][int(column)])
    output = "".join(output)
    print('Transposed output is: ',output)
    return output

def Prep_Decipher(input, key):
    key = Normalize_key(key)    
    input = input.split(' ')
    input.pop(len(input) - 1)

    unsorted_key = key
    unsorted_key = list(unsorted_key.strip(""))
    key = sorted(key)

    key_index = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i] == unsorted_key[j]:
                key_index.append(j)
                unsorted_key[j] = ' '

    max = len(input[0])
    min = max
    for i in input:
        if len(i) > max: max = len(i)
        if len(i) < min: min = len(i)

    for_decipher = []
    for i in range(min):
        for j in range(len(key_index)):
            index = key_index.index(j)
            for_decipher.append(input[index][i])

    for i in range(len(key_index)):
        if max == min: break
        index = key_index.index(i)
        if len(input[index]) == max:
            for_decipher.append(input[index][max - 1])

    for_decipher = ''.join(for_decipher)
    return for_decipher

def Trans_Doubles(a,grid):
    if a.isdigit(): return a
    if len(grid) == 5:
        match a:
                case 'A': return 0
                case 'D': return 1
                case 'F': return 2
                case 'G': return 3
                case 'X': return 4
                case '_': return ' '
    if len(grid) == 6:
        match a:
                case 'A': return 0
                case 'D': return 1
                case 'F': return 2
                case 'G': return 3
                case 'V': return 4
                case 'X': return 5
                case '_': return ' '

def Decipher(input,grid,key):
    input = Prep_Decipher(input,key)
    output = []
    i = 0
    while i < len(input):
        if i == len(input) - 1 and input[len(input) - 1].isdigit(): output.append(input[len(input) - 1])
        if i < len(input) - 1:
            a = Trans_Doubles(input[i],grid)
            b = Trans_Doubles(input[i + 1],grid)
            if a == ' ' or input[i].isdigit(): output.append(a); i+=1; continue
            if b == ' ' or input[i + 1].isdigit(): output.append(b); i+=1; continue
            output.append(grid[a][b])
            i += 2
        else: break

    output = ''.join(output)
    return output