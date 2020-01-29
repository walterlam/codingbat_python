# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:56:22 2020

@author: walter
"""

def cigar_party(cigars, is_weekend):
    '''
    When squirrels get together for a party, they like to have cigars. 
    A squirrel party is successful when the number of cigars is between 40 
    and 60, inclusive. Unless it is the weekend, in which case there is no 
    upper bound on the number of cigars. Return True if the party with the 
    given values is successful, or False otherwise.
    
    cigar_party(30, False) → False
    cigar_party(50, False) → True
    cigar_party(70, True) → True
    '''
    if is_weekend and cigars >= 40:
        return True
    elif (not is_weekend) and 40 <= cigars <= 60:
        return True
    else:
        return False

def date_fashion(you, date):
    '''
    You and your date are trying to get a table at a restaurant. 
    The parameter "you" is the stylishness of your clothes, in the range 0..10,
    and "date" is the stylishness of your date's clothes. 
    The result getting the table is encoded as an int value with 
    0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, 
    then the result is 2 (yes). With the exception that if either of you has
    style of 2 or less, then the result is 0 (no). 
    Otherwise the result is 1 (maybe).
    
    date_fashion(5, 10) → 2
    date_fashion(5, 2) → 0
    date_fashion(5, 5) → 1
    '''
    if you <=2 or date <=2:
        return 0
    elif you >=8 or date >=8:
        return 2
    else:
        return 1
    
def squirrel_play(temp, is_summer):
    '''
    The squirrels in Palo Alto spend most of the day playing. 
    In particular, they play if the temperature is between 60 and 90 
    (inclusive). Unless it is summer, then the upper limit is 100 instead of 
    90. Given an int temperature and a boolean is_summer, return True if the 
    squirrels play and False otherwise.
    
    squirrel_play(70, False) → True
    squirrel_play(95, False) → False
    squirrel_play(95, True) → True
    '''
    if is_summer:
        return (60 <= temp <= 100)
    else:
        return (60 <= temp <= 90)

def caught_speeding(speed, is_birthday):
    '''
    You are driving a little too fast, and a police officer stops you. 
    Write code to compute the result, encoded as an int value: 0=no ticket, 
    1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
    If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 
    or more, the result is 2. Unless it is your birthday -- on that day,
    your speed can be 5 higher in all cases.
    
    caught_speeding(60, False) → 0
    caught_speeding(65, False) → 1
    caught_speeding(65, True) → 0
    '''
    benchmark1 = 60
    benchmark2 = 80
    if is_birthday:
        if speed <= benchmark1 +5:
            return 0
        elif benchmark1+5 < speed <= benchmark2+5:
            return 1
        else:
            return 2
    else:
        if speed <= benchmark1:
            return 0
        elif benchmark1 < speed <= benchmark2:
            return 1
        else:
            return 2

def sorta_sum(a, b):
    '''
    Given 2 ints, a and b, return their sum. However, sums in the range 
    10..19 inclusive, are forbidden, so in that case just return 20.
    
    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21
    '''
    if 10 <= a+b < 20:
        return 20
    else:
        return a+b

def alarm_clock(day, vacation):
    '''
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
    and a boolean indicating if we are on vacation, 
    return a string of the form "7:00" indicating when the alarm clock 
    should ring. Weekdays, the alarm should be "7:00" and on the weekend 
    it should be "10:00". Unless we are on vacation -- then on weekdays 
    it should be "10:00" and weekends it should be "off".
    
    alarm_clock(1, False) → '7:00'
    alarm_clock(5, False) → '7:00'
    alarm_clock(0, False) → '10:00'
    '''
    if vacation:
        if day in range(1,6):
            return '10:00'
        else:
            return 'off'
    else:
        if day in range(1,6):
            return '7:00'
        else:
            return '10:00'

def love6(a, b):
    '''
    The number 6 is a truly great number. Given two int values, a and b, 
    return True if either one is 6. Or if their sum or difference is 6. 
    Note: the function abs(num) computes the absolute value of a number.
    
    love6(6, 4) → True
    love6(4, 5) → False
    love6(1, 5) → True
    '''
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
    '''
    Given a number n, return True if n is in the range 1..10, inclusive. 
    Unless outside_mode is True, in which case return True if the number 
    is less or equal to 1, or greater or equal to 10.
    
    in1to10(5, False) → True
    in1to10(11, False) → False
    in1to10(11, True) → True
    '''
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

def near_ten(num):
    '''
    Given a non-negative number "num", return True if num is within 2 of 
    a multiple of 10. Note: (a % b) is the remainder of dividing a by b, 
    so (7 % 5) is 2. See also: Introduction to Mod
    
    near_ten(12) → True
    near_ten(17) → False
    near_ten(19) → True
    '''
    if num%10 <=2 or 10-num%10 <=2:
        return True
    return False