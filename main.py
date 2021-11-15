#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:
# Autor:
############################################################################
from random import randint, choice
from os.path import exists

############################################################################


def a():
    vstup = input('vstupní soubor > ')
    if exists(vstup):
        pass
    print('A')

def b():
    print('B')
    

if __name__ == "__main__":
    print("""
    Co chceš dělat?
    1) převod souboru na malá písmena
    2) nahrazení znaku v souboru
    3) ...........
    """)
    while True:
        volba = input('Zadej svou volbu > ')
        if volba.isdigit():
            volba = int(volba)
            break
    if volba==1:
        vstup.write(data.lower())
    elif volba==2:
        with open(vstup, 'r+') as f:

            vstup = f.read()
    
            replace_string = vstup.replace(input('Zadej znak, který chceš nahradit: '), input('Zadej znak, který ho nahradí: '))
    
            f.write(replace_string)
    else:
        print('nic')