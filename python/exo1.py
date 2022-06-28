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
