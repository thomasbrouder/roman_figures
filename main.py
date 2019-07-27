def get_roman_compose(input, nb_zeros):
    '''
    Function to translate a number of form a000 where 0 < a < 9 into a roman number
    :param input: number of base 10 to translate
    :param nb_zeros: number of zeros in the number, ex: input = 2000 --> nb_zeros = 3
    :return: Roman number
    '''
    roman_char = {0: ('I', 'V', 'X'), 1: ('X', 'L', 'C'), 2: ('C', 'D', 'M'), 3: ('M', None), 4: (None, None)}
    one = roman_char[nb_zeros]
    figure = int(str(input)[0:2])
    if figure == 10:
        roman = 'X'
    else:
        figure = int(str(input)[0])
        if figure == 0:
            roman = ''
        if figure in [1, 2, 3]:
            roman = one[0] * figure
        elif figure in [4, 5]:
            roman = one[0] * (5 - figure) + one[1]
        elif figure in [6, 7, 8]:
            roman = one[0] * (5 - figure) + one[1] + one[0] * (figure - 5)
        elif figure in [9]:
            roman = one[0] + one[2]
    return roman

def get_roman(input):
    '''
    Function to translate any number between 1 and 3999 into a roman number.
    This function decomposes the input number into several simple numbers that can be translated into roman numbers
    with the get_roman_compose function. ex: 3999 = 3000 + 900 + 99 + 9 = 'MMM' + 'CM' + 'XC' + 'IX
    :param input: number in base 10, between 1 and 3999
    :return: roman number
    '''
    roman_max = 3999
    if input > roman_max:
        print("{} is higher than maximum roman figure {}".format(input, roman_max))
        exit()
    roman_compose = []
    for i in range(len(str(input))):
        figure = int(str(input)[i])
        nb_zeros = len(str(input)[i:]) - 1
        roman_compose.append(get_roman_compose(figure, nb_zeros))
    roman = ''
    for roman_figure in roman_compose:
        roman += roman_figure
    return roman

def generate_romans(max):
    '''
    Function to translate and store every numbers from 1 to max into roman numbers
    :param max: maximum number to be translated
    :return: roman_dict, dictionnary {base_ten : roman}
    '''
    roman_dict = {}
    for input in range(1, max + 1):
        roman_dict[input] = get_roman(input)
    return roman_dict

if __name__ == '__main__':
    roman = get_roman(2019)
    print(roman)
    roman_dict = generate_romans(max=3999)
