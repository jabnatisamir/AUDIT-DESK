#!/usr/bin/env python3
"""CLI to generate audit dossier workbooks.

Usage:
    python generate.py                    # Generate for SOC_COM (default)
    python generate.py SOC_COM            # Generate for societe commerciale
    python generate.py HOLDING            # Generate for holding
    python generate.py ASSO              # Generate for association
    python generate.py ESS               # Generate for ESS
    python generate.py SPECTACLE         # Generate for spectacle vivant
    python generate.py COOP              # Generate for cooperative
    python generate.py --all             # Generate for all profiles
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.generator import generate_dossier, generate_all_profils


PROFILS_VALIDES = ["SOC_COM", "HOLDING", "ASSO", "ESS", "SPECTACLE", "COOP"]


def main():
    if len(sys.argv) < 2:
        profil = "SOC_COM"
    elif sys.argv[1] == "--all":
        generate_all_profils()
        return
    elif sys.argv[1] == "--help":
        print(__doc__)
        print(f"Profils disponibles: {', '.join(PROFILS_VALIDES)}")
        return
    else:
        profil = sys.argv[1].upper()
        if profil not in PROFILS_VALIDES:
            print(f"Profil inconnu: {profil}")
            print(f"Profils disponibles: {', '.join(PROFILS_VALIDES)}")
            sys.exit(1)

    generate_dossier(profil_code=profil)


if __name__ == "__main__":
    main()
