# AUDIT-DESK

Outil de gestion et de formalisation de la mission de commissariat aux comptes (CAC).
Generateur de dossiers d'audit Excel conformes NEP, fondes sur l'approche par les risques.

## Architecture

```
AUDIT-DESK/
  referentiel/          # Donnees de reference JSON (cycles, assertions, risques, controles, profils, seuils, programmes)
  engine/               # Moteur Python de generation Excel
    styles.py           # Styles, couleurs, formatage
    data_loader.py      # Chargement des referentiels JSON
    generator.py        # Assemblage du classeur dossier mission
    parametres_cabinet.py # Generation du classeur parametres cabinet
    sheets/             # Generateurs par onglet
      accueil.py        # Page d'accueil dossier
      acceptation.py    # Acceptation/maintien + Prise de connaissance
      seuils.py         # Determination des seuils de signification
      matrice_risques.py # Matrice des risques d'anomalies significatives
      controle_interne.py # Controle interne, ITGC, ITAC
      cycle_travail.py  # Feuilles de travail par cycle
      synthese.py       # Feuilles maitresses, anomalies, synthese, finalisation
      gestion_cabinet.py # Temps, rentabilite, dashboard COPIL
  config/               # Templates de configuration mission
  output/               # Fichiers Excel generes (gitignored)
  generate.py           # Point d'entree CLI
```

## Utilisation

```bash
pip install openpyxl
python generate.py              # Societe commerciale (defaut)
python generate.py HOLDING      # Holding
python generate.py ASSO         # Association
python generate.py ESS          # ESS
python generate.py SPECTACLE    # Spectacle vivant
python generate.py COOP         # Cooperative
python generate.py --all        # Tous les profils
```

## Profils d'entites

6 profils sectoriels avec risques, questionnaires et controles specifiques :
- `SOC_COM` : Societe commerciale (12 cycles, 28 onglets)
- `HOLDING` : Holding (11 cycles, 27 onglets)
- `ASSO` : Association (10 cycles, 26 onglets)
- `ESS` : Economie sociale et solidaire (10 cycles, 26 onglets)
- `SPECTACLE` : Spectacle vivant (10 cycles, 26 onglets)
- `COOP` : Cooperative (12 cycles, 28 onglets)

## Modules du dossier

A. Pilotage : Accueil, Dashboard COPIL/ISO
B. Approche : Acceptation, Prise de connaissance, Seuils, Matrice des risques
C. Controle interne : Controles cles, ITGC, ITAC
D. Cycles : 1 onglet par cycle avec risques, programme de travail, tests, synthese
E. Finalisation : Feuilles maitresses, Anomalies, Synthese generale, Points de revue, Check-list
F. Gestion cabinet : Temps, Rentabilite / Boni-Mali

## Referentiels

Les donnees sont dans `referentiel/*.json` et peuvent etre enrichies :
- `cycles.json` : 12 cycles d'audit avec comptes PCG
- `assertions.json` : assertions par categorie (flux, soldes, presentation)
- `risques.json` : 20 risques generaux + 2 risques de fraude NEP 240
- `controles.json` : 15 controles cles + 4 ITGC + 4 ITAC
- `profils_entites.json` : 6 profils avec risques sectoriels
- `programmes_travail.json` : procedures d'audit par cycle avec regles de selection
- `seuils.json` : methodes de calcul des seuils par type d'entite

## Conventions de code

- Python 3.8+, openpyxl
- Pas d'accents dans les identifiants Python, accents dans les labels Excel
- Les zones de saisie utilisateur sont en jaune clair (fill_input)
- Les zones calculees sont en gris clair (fill_calculated)
- Les niveaux de risque sont colores : vert (Faible), jaune (Modere), orange (Eleve), rouge (Significatif)
