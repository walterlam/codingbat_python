def string_times(str, n):
    '''
    Given a string and a non-negative int n, return a larger string that is 
    n copies of the original string.
    
    string_times('Hi', 2) → 'HiHi'
    string_times('Hi', 3) → 'HiHiHi'
    string_times('Hi', 1) → 'Hi'
    '''
    str2 = ''
    for i in range(n):
        str2 = str2 + str
    return str2

def front_times(str, n):
    '''
    Given a string and a non-negative int n, we'll say that the front of the 
    string is the first 3 chars, or whatever is there if the string is less 
    than length 3. Return n copies of the front.
    
    front_times('Chocolate', 2) → 'ChoCho'
    front_times('Chocolate', 3) → 'ChoChoCho'
    front_times('Abc', 3) → 'AbcAbcAbc'
    '''
    if len(str) <= 3:
        front = str
    else:
        front = str[0:3]
    str2 = ''
    for i in range(n):
        str2 += front
    return str2

def string_bits(str):
    '''
    Given a string, return a new string made of every other char starting with
    the first, so "Hello" yields "Hlo".
    
    string_bits('Hello') → 'Hlo'
    string_bits('Hi') → 'H'
    string_bits('Heeololeo') → 'Hello'
    '''
    str2 = str[::2]
    return str2

def string_bits2(str):
    '''
    Loop version of string_bits(str)
    '''
    str2 = ''
    for i in range(0, len(str), 2):
        str2 += str[i]
    return str2

def string_splosion(str):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    
    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
    '''
    result = ''
    for i in range(len(str)):
        for j in range(i+1):
            result = result + str[j]
    return result


