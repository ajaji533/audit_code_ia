def calculatrice():
    expression = input("Entrez une opération : ")
    try:
        resultat = eval(expression)
        print("Résultat :", resultat)
    except Exception as e:
        print("Erreur :", e)

def menu():
    print("Mini calculatrice")
    calculatrice()

if __name__ == "__main__":
    menu()
