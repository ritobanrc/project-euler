#!/usr/bin/env python3

names = {
    1: 'one', 
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve', 
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen', 
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fify',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def num2word(num):
    word = ''
    if num >= 1000:
        word += names[int(str(num)[0])]
        word += 'thousand'
    num = int(str(num)[1:])
    if num > 100:
        g

import random

for _ in range(20):
    n = random.randint(1, 1000)
    print(n, num2word(n))
