import functions


my_input = ["A","B","C","D"]
print(my_input)
ascii = functions.convert_char_to_ascii(my_input)
print(ascii)
binary = functions.ascii_to_binary(ascii)
print(binary)
octet = functions.binary_to_octet(binary)
print(octet)