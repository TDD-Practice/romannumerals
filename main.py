def toroman(number):
    table = {1: 'I',2: 'II',3: 'III',4: 'IV',5: 'V',6: 'VI',7: 'VII',8: 'VIII',9: 'IX',10: 'X'}
    if number < 10:
        return table[number]
    if number % 10 == 0:
        return 'X' * (number//10)
    if number < 20:
        return 'X' + table[number%10]


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
