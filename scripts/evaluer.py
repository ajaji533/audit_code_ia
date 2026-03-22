import csv
import sys
from pathlib import Path

def lire_csv(chemin):
    with open(chemin, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def ecrire_csv(chemin, entetes, lignes):
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(entetes)
        writer.writerows(lignes)

def evaluer(verite_csv, outil_csv, sortie_csv):
    verite = lire_csv(verite_csv)
    resultats = lire_csv(outil_csv)

    verite_map = {}
    for ligne in verite:
        verite_map[ligne["fichier"]] = {
            "langage": ligne["langage"],
            "attendu": ligne["type_probleme"],
            "gravite": ligne["gravite"],
            "description": ligne["description_attendue"],
            "source": ligne["source"],
        }

    resultat_map = {}
    for ligne in resultats:
        resultat_map[ligne["fichier"]] = {
            "detecte": ligne["probleme_detecte"].strip(),
            "gravite_proposee": ligne["gravite_proposee"].strip(),
            "justification": ligne["justification"].strip(),
        }

    tp = 0
    fp = 0
    fn = 0

    lignes_synthese = []

    for fichier, infos in verite_map.items():
        attendu = infos["attendu"]
        langage = infos["langage"]
        gravite_attendue = infos["gravite"]

        detecte = ""
        gravite_detectee = ""
        justification = ""

        if fichier in resultat_map:
            detecte = resultat_map[fichier]["detecte"]
            gravite_detectee = resultat_map[fichier]["gravite_proposee"]
            justification = resultat_map[fichier]["justification"]

        if detecte == attendu:
            statut = "OK"
            tp += 1
        elif detecte == "":
            statut = "NON_DETECTE"
            fn += 1
        else:
            statut = "MAUVAIS_TYPE"
            fp += 1
            fn += 1

        lignes_synthese.append([
            fichier,
            langage,
            attendu,
            gravite_attendue,
            detecte if detecte else "rien",
            gravite_detectee if gravite_detectee else "rien",
            statut,
            justification if justification else "Aucune justification"
        ])

    precision = tp / (tp + fp) if (tp + fp) else 0
    rappel = tp / (tp + fn) if (tp + fn) else 0

    ecrire_csv(
        sortie_csv,
        [
            "fichier",
            "langage",
            "probleme_attendu",
            "gravite_attendue",
            "probleme_detecte",
            "gravite_detectee",
            "statut",
            "justification",
        ],
        lignes_synthese
    )

    print("=== RESULTATS ===")
    print(f"Fichier outil     : {outil_csv}")
    print(f"Fichier synthese  : {sortie_csv}")
    print(f"Vrais positifs    : {tp}")
    print(f"Faux positifs     : {fp}")
    print(f"Faux negatifs     : {fn}")
    print(f"Precision         : {precision:.2f}")
    print(f"Rappel            : {rappel:.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 scripts/evaluer.py <verite_terrain.csv> <outil.csv> <sortie_synthese.csv>")
        sys.exit(1)

    verite_csv = sys.argv[1]
    outil_csv = sys.argv[2]
    sortie_csv = sys.argv[3]

    Path("rapports").mkdir(exist_ok=True)

    evaluer(verite_csv, outil_csv, sortie_csv)
