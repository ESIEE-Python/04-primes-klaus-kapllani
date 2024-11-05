# main.py
"""
author = klaus.kapllani@esiee.fr
"""

from math import sqrt

def isprime(p):
    """
    Détermine si p est premier.

    Args : 
        p : valeur entiere positive

    Returns :
        isprime(p) : True si c'est un nombre premier, sinon False
    """
    # Si p est inférieur à 1, ce n'est pas un nombre premier
    if p <= 1:
        return False
    # Sinon, on vérifie tous les diviseurs jusqu'à la racine carrée de n
    for i in range(2, int(sqrt(p)) + 1):
        if p%i == 0:
            return False
    return True

def main():
    """
    Fonction principale qui affiche les nombres premier entre 1 et 100.

    Returns :
        rien
    """
    print("Nombres premiers entre 1 et 100 : ", [n for n in range(100) if isprime(n)])

if __name__ == "__main__":
    main()
