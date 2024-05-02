"""Below program converts a Roman Number to its corresponding integer"""

def convert_roman_to_integer(roman):
    #define a hash map with key value pairs of romans and integers
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    output = 0

    #to handle values like 4, 9, 40, 90, 400 and 900 we replace their corresponding romans into below forms, as it becomes to traverse through string and identify these numbers
    roman = roman.replace('IV','IIII').replace('IX','VIIII')
    roman = roman.replace('XL','XXXX').replace('XC','LXXX')
    roman = roman.replace('CD','CCCC').replace('CM','DCCCC')

    for char in roman:
        output += roman_to_int[char]
    return output

print(convert_roman_to_integer('MMMMMMMMMCMXCIX')) #this will print 9989
