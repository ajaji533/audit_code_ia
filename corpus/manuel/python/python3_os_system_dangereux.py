import os

def lister_dossier():
    nom = input("Nom du dossier à lister : ")
    commande = "ls " + nom
    os.system(commande)

if __name__ == "__main__":
    lister_dossier()
