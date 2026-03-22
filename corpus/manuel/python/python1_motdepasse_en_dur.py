DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "supersecret123"

def connecter_base():
    print(f"Connexion à {DB_HOST} avec l'utilisateur {DB_USER}...")
    if DB_PASSWORD:
        print("Connexion réussie")
    else:
        print("Mot de passe manquant")

def afficher_statut():
    print("Application prête")

if __name__ == "__main__":
    afficher_statut()
    connecter_base()
