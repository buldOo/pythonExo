# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    annee = int(input("Entrez l annee a verifier:"))
    if (annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0):
        print("L'annee est une annee bissextile!")
    else:
        print("L'annee n'est pas une annee bissextile!")