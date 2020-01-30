def double_char(str):
    '''
    Given a string, return a string where for every char in the original, 
    there are two chars.
    
    double_char('The') → 'TThhee'
    double_char('AAbb') → 'AAAAbbbb'
    double_char('Hi-There') → 'HHii--TThheerree'
    '''
    result=''
    for char in str:
        result += char*2
    return result

def count_hi(str):
    '''
    Return the number of times that the string "hi" appears anywhere in 
    the given string.
    
    count_hi('abc hi ho') → 1
    count_hi('ABChi hi') → 2
    count_hi('hihi') → 2
    '''
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            count += 1
    return count

def cat_dog(str):
    '''
    Return True if the string "cat" and "dog" appear the same number of 
    times in the given string.
    
    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True
    '''
    count_cat = 0
    count_dog = 0
    for i in range(len(str)-2):
        if str[i:i+3] == 'cat':
            count_cat += 1
        if str[i:i+3] == 'dog':
            count_dog += 1
    return (count_cat == count_dog)

def count_code(str):
    '''
    Return the number of times that the string "code" appears anywhere in the 
    given string, except we'll accept any letter for the 'd', so "cope" 
    and "cooe" count.
    
    count_code('aaacodebbb') → 1
    count_code('codexxcode') → 2
    count_code('cozexxcope') → 2
    '''
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count

def end_other(a, b):
    '''
    Given two strings, return True if either of the strings appears at the 
    very end of the other string, ignoring upper/lower case differences (in 
    other words, the computation should not be "case sensitive"). 
    Note: s.lower() returns the lowercase version of a string.
    
    end_other('Hiabc', 'abc') → True
    end_other('AbC', 'HiaBc') → True
    end_other('abc', 'abXabc') → True
    '''
    a_new = a.lower()
    b_new = b.lower()
    
    (str,minlen) = a_or_b_shorter(a_new,b_new)
    if str == a_new:
        if b_new[-minlen:] == str:
            return True
        else:
            return False
    else:
        if a_new[-minlen:] == str:
            return True
        else:
            return False
  
def a_or_b_shorter(a, b):
    if len(a) <= len(b):
        return (a,len(a))
    return (b,len(b))

def xyz_there(str):
    '''
    Return True if the given string contains an appearance of "xyz" 
    where the xyz is not directly preceeded by a period (.). 
    So "xxyz" counts but "x.xyz" does not.

    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True
    
    3 cases:
        '.xyz': move 4 chars
        'xyz': return True
        others: move to next char for checking
    '''
    if 'xyz' not in str:
        return False
    
    i = 0
    while i < len(str):
        if str[i:i+4] == '.xyz':
            i = i+4
        elif str[i:i+3] == 'xyz':
            return True
        else:
            i += 1
    return False
    
