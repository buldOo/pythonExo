import functions

my_input = ["A","B","C","D"]
print(my_input)

#Ascii
ascii = functions.convert_char_to_ascii(my_input)
print("Ascii values :", ascii)

#Binary
binary = functions.ascii_to_binary(ascii)
print("Binaries values :", binary)

#Octet
octet = functions.binary_to_octet(binary)
print("Octet values :", octet)

#String
string = functions.binary_to_string(octet)
print("String value :", string)