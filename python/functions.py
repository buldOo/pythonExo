def convert_char_to_ascii(char_to_convert):
    """A function convert characteres to ascii values

    :param char_to_convert: array of characteres
    :return char_ascii: array of ascii values
    """
    char_ascii = []
    for char_to_convert in char_to_convert:
        char_ascii.append(ord(char_to_convert))
    return char_ascii


def ascii_to_binary(values_to_convert):
    """ A function ton convert ascii number into binary number

    :param values_to_convert: An array of value to convert
    :return: An array of binary values
    """
    binarys = []
    for value_to_convert in values_to_convert:
        binarys.append(format(value_to_convert, "b"))
    return binarys


def binary_to_octet(char_binary):
    """Change binary number to one octet
    :param: char_binary
    :return: octet
    """
    char_octet = []
    for char_binary in char_binary:
        char_octet.append("0" + char_binary)
    return char_octet


def binary_to_string(array):
    string_to_return = ""
    for index in array:
        string_to_return = string_to_return + index

    return string_to_return


def string_to_bit(string_to_convert):
    """ A function ton convert a string into an array of bit

    :param string_to_convert: The string to convert into bit
    :return: The converted string
    """
    converted_strings = []
    start = 0
    end = 6

    while len(string_to_convert) % 6 != 0:
        string_to_convert = string_to_convert + "0"

    for i in range(6 % len(string_to_convert)):
        converted_strings.append(string_to_convert[start:end])
        start = start + 6
        end = end + 6

    return converted_strings


def decimal_to_hexa(decimal_list):
    """Convert decimal to hexadecimal

    :param decimal:
    :return hexa_list:
    """
    hexa_list = []

    base64_dict = {"110000": "w", "110001": "x", "110101": "1", "110100": "0", "010100": "U", "010101": "V", "001100": "M", "001101": "N", "011110": "e", "011111": "f", "001001": "J", "001000": "I", "011011": "b", "011010": "a", "000110": "G", "000111": "H", "000011": "D", "000010": "C", "100100": "k", "100101": "l", "111100": "8", "111101": "9", "100010": "i", "100011": "j", "101110": "u", "101111": "v", "111001": "5", "111000": "4", "101011": "r", "101010": "q", "110011": "z", "110010": "y", "010010": "S", "010011": "T", "010111": "X", "010110": "W", "110110": "2", "110111": "3", "011000": "Y", "011001": "Z", "001111": "P", "001110": "O", "011101": "d", "011100": "c", "001010": "K", "001011": "L", "101101": "t", "000000": "A", "000001": "B", "100111": "n", "100110": "m", "000101": "F", "000100": "E", "111111": "/", "111110": "+", "100001": "h", "100000": "g", "010001": "R", "010000": "Q", "101100": "s", "111010": "6", "111011": "7", "101000": "o", "101001": "p"}


    for decimal_list in decimal_list:

        print(format(decimal_list, "b"))
        hexa_list.append(hex(decimal_list))
    return hexa_list