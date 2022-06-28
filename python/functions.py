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
