def ascii_to_binary(values_to_convert):
    """ A function ton convert ascii number into binary number

    :param values_to_convert: An array of value to convert
    :return: An array of binary values
    """
    print(len(values_to_convert))
    binarys = []
    for value_to_convert in values_to_convert:
        binarys.append(format(value_to_convert, "b"))
    return binarys


def convert_char_to_ascii(char_to_convert):
    char_ascii = ord(char_to_convert)
    return char_ascii
