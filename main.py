def toroman(number):
    table_units = {0: "", 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    table_tens = {0: "", 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    table_hundreds = {0: "", 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
    number_units = number % 10
    number_tens = number//10 % 10
    number_hundreds = number//100 % 10
    
    roman_units = table_units[number_units]
    roman_tens = table_tens[number_tens]
    roman_hundreds = table_hundreds[number_hundreds]

    return roman_hundreds + roman_tens + roman_units


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
        elif roman[i:i+1] == "V":
            number += 5
            i+=1
            if roman[i:i+1] == "I":
                number -= 1
                i+=1
        elif roman[i:i+1] == "X":
            number += 10
            i+=1
            if roman[i:i+1] == "I":
                number -= 1
                i+=1
        else: raise ValueError("Invalid Roman number")
    return number
