def toroman(number):
    table_units = {0: "", 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    table_tens = {0: "", 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    roman = ""
    number_units = number % 10
    number_tens = number//10 % 10
    
    roman_units = table_units[number_units]
    roman_tens = table_tens[number_tens]

    return roman_tens + roman_units


def fromroman(roman):
    roman = roman[::-1]
    number = 0
    i=0
    while i < len(roman):
        if roman[i:i+1] == "I":
            number += 1
            i+=1
            if roman[i:i+1] == "I":
                number += 1
                i+=1
            if roman[i:i+1] == "I":
                number += 1
                i+=1
        if roman[i:i+1] == "V":
            number += 5
            i+=1
            if roman[i:i+1] == "I":
                number -= 1
                i+=1
        if roman[i:i+1] == "X":
            number += 10
            i+=1
            if roman[i:i+1] == "I":
                number -= 1
                i+=1
    return number
