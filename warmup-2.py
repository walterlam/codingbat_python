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

def last2(str):
    '''
    Given a string, return the count of the number of times that a substring 
    length 2 appears in the string and also as the last 2 chars of the string,
    so "hixxxhi" yields 1 (we won't count the end substring).
    
    last2('hixxhi') → 1
    last2('xaxxaxaxx') → 1
    last2('axxxaaxx') → 2
    '''
    if len(str) < 2:
        return 0
    else:
        count = 0
        check = str[-2:]
        for i in range(len(str)-2):
            if str[i:i+2] == check:
                count +=1
        return count

def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.
    
    array_count9([1, 2, 9]) → 1
    array_count9([1, 9, 9]) → 2
    array_count9([1, 9, 9, 3, 9]) → 3
    '''
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

def array_front9(nums):
    '''
    Given an array of ints, return True if one of the first 4 elements in the 
    array is a 9. The array length may be less than 4.
    
    array_front9([1, 2, 9, 3, 4]) → True
    array_front9([1, 2, 3, 4, 9]) → False
    array_front9([1, 2, 3, 4, 5]) → False
    '''
    checknum = min(4,len(nums))
    for i in range(checknum):
        if nums[i] == 9:
            return True
    return False

def array123(nums):
    '''
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 
    appears in the array somewhere.
    
    array123([1, 1, 2, 3, 1]) → True
    array123([1, 1, 2, 4, 1]) → False
    array123([1, 1, 2, 1, 2, 3]) → True
    '''
    if len(nums) < 3:
        return False
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

def string_match(a, b):
    '''
    Given 2 strings, a and b, return the number of the positions where they 
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
    since the "xx", "aa", and "az" substrings appear in the same place in 
    both strings.
    
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0
    '''
    check = min(len(a),len(b))
    count = 0
    for i in range(check-1):
        if a[i] == b[i] and a[i+1] == b[i+1]:
            count += 1
    return count
