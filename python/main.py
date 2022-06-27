import functions

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 1
    while i == 1:
        annee = int(input("Entrez l annee a verifier:"))
        if (annee == 0000):
            print("A la prochaine")
            i = 0
        elif (annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0):
            print("L'annee est une annee bissextile!")
        else:
            print("L'annee n'est pas une annee bissextile!")

    my_input = [64, 64, 65]
    print(functions.ascii_to_binary(my_input))
