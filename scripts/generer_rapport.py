import csv
from pathlib import Path

FICHIERS_OUTILS = {
    "SonarQube": "rapports/synthese_sonarqube.csv",
    "Snyk": "rapports/synthese_snyk.csv",
    "CodeQL": "rapports/synthese_codeql.csv",
}

SORTIE_CSV = "rapports/synthese.csv"
SORTIE_MD = "rapports/rapport.md"

def lire_csv(chemin):
    with open(chemin, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def ecrire_csv(chemin, entetes, lignes):
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(entetes)
        writer.writerows(lignes)

def calculer_stats(lignes):
    ok = 0
    non_detecte = 0
    mauvais_type = 0

    for ligne in lignes:
        statut = ligne["statut"].strip()
        if statut == "OK":
            ok += 1
        elif statut == "NON_DETECTE":
            non_detecte += 1
        elif statut == "MAUVAIS_TYPE":
            mauvais_type += 1

    total = len(lignes)
    precision = ok / (ok + mauvais_type) if (ok + mauvais_type) else 0
    rappel = ok / (ok + non_detecte + mauvais_type) if total else 0

    return {
        "total": total,
        "ok": ok,
        "non_detecte": non_detecte,
        "mauvais_type": mauvais_type,
        "precision": precision,
        "rappel": rappel,
    }

def main():
    Path("rapports").mkdir(exist_ok=True)

    lignes_csv = []

    with open(SORTIE_MD, "w", encoding="utf-8") as md:
        md.write("# Rapport d'évaluation des outils d'audit de code\n\n")
        md.write("## Objectif\n")
        md.write("Comparer plusieurs outils d'audit de code sur un corpus manuel annoté.\n\n")
        md.write("## Outils évalués\n")
        md.write("- SonarQube\n")
        md.write("- Snyk\n")
        md.write("- CodeQL\n\n")

        md.write("## Résultats globaux\n\n")
        md.write("| Outil | Total | OK | Non détecté | Mauvais type | Précision | Rappel |\n")
        md.write("|---|---:|---:|---:|---:|---:|---:|\n")

        for outil, chemin in FICHIERS_OUTILS.items():
            lignes = lire_csv(chemin)
            stats = calculer_stats(lignes)

            lignes_csv.append([
                outil,
                stats["total"],
                stats["ok"],
                stats["non_detecte"],
                stats["mauvais_type"],
                f'{stats["precision"]:.2f}',
                f'{stats["rappel"]:.2f}',
            ])

            md.write(
                f"| {outil} | {stats['total']} | {stats['ok']} | "
                f"{stats['non_detecte']} | {stats['mauvais_type']} | "
                f"{stats['precision']:.2f} | {stats['rappel']:.2f} |\n"
            )

        md.write("\n## Interprétation\n\n")
        md.write("- **OK** : le problème attendu a bien été détecté.\n")
        md.write("- **Non détecté** : l'outil n'a rien trouvé alors qu'un problème était attendu.\n")
        md.write("- **Mauvais type** : l'outil a détecté quelque chose, mais pas le bon problème.\n")

    ecrire_csv(
        SORTIE_CSV,
        ["outil", "total", "ok", "non_detecte", "mauvais_type", "precision", "rappel"],
        lignes_csv
    )

    print("Rapports générés avec succès :")
    print(f"- {SORTIE_CSV}")
    print(f"- {SORTIE_MD}")

if __name__ == "__main__":
    main()
