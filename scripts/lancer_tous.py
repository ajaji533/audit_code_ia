import subprocess

commandes = [
    [
        "python3",
        "scripts/evaluer.py",
        "verite_terrain.csv",
        "outils/sonarqube.csv",
        "rapports/synthese_sonarqube.csv"
    ],
    [
        "python3",
        "scripts/evaluer.py",
        "verite_terrain.csv",
        "outils/snyk.csv",
        "rapports/synthese_snyk.csv"
    ],
    [
        "python3",
        "scripts/evaluer.py",
        "verite_terrain.csv",
        "outils/codeql.csv",
        "rapports/synthese_codeql.csv"
    ]
]

for cmd in commandes:
    print("Lancement :", " ".join(cmd))
    subprocess.run(cmd, check=True)

print("\nTous les outils ont été évalués avec succès.")
