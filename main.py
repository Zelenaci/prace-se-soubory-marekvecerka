#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:
# Autor:
############################################################################
from random import randint, choice
from os.path import exists

############################################################################

samohlasky = 'aeiouy'
souhlasky = 'qwrtzpsdfghjklxcvbnm'

print("""
Zadejte volbu:
1) Chcete měnit soubory?
2) Chcete generovat náhodný text?
""")
prvnivolba=int(input("Zadejte číslo volby: "))    

if prvnivolba==1:
    
    if __name__ == "__main__":
        print("""
        Co chceš dělat?
        1) převod souboru na malá písmena
        2) nahrazení znaku v souboru
        3) Spočítat jednotlivé znaky v souboru
        """)
    while True:
            volba = input('Zadej svou volbu > ')
            if volba.isdigit():
                volba = int(volba)
                break
    if volba==1:
            def mala():

                soubor1=open(input("Zadejte cestu k pracovnímu souboru: "),"r")
                obsah=soubor1.read()
                soubor2=open(input("Zadejte název výstupního souboru: "),"w")
             
                prepis=obsah.lower()
                vystup=soubor2.write(prepis)
                print("""
            Soubor byl přepsán na malé písmena.
            """)

            """elif volba==2:
            
                soubor1=open(input("Zadejte cestu k pracovnímu souboru: "),"r")
        
                nahrad = soubor1.replace(input('Zadej znak, který chceš nahradit: '), input('Zadej znak, který ho nahradí: '))
        
                f.write(nahrad)     """
    
    elif volba==2:

        soubor1=open(input("Zadejte cestu k pracovnímu souboru: "),"r")
        soubor2=open(input("Zadejte název výstupního souboru: "),"w")

        najdi = input('Zadej písmeno, které chceš změnit: ')
        nahrad = input('Zadej písmeno, kterým ho chceš nahradit: ')

        with open(soubor1, 'r') as file:
            data = file.read()
            data = data.replace(najdi, nahrad)

        with open(soubor2, 'w') as file:
            file.write(data)
        print("Hotovo.")

    elif volba==3:  

        soubor1=open(input("Zadejte cestu k pracovnímu souboru: "),"r")
        obsah=soubor1.read()
        soubor2=open(input("Zadejte název výstupního souboru: "),"w") 
    
        
        pismena=dict()
        
        while True:
            znak = obsah.read(1).upper()
            if znak == '':
                break
            elif znak in pismena.keys():
                pismena[znak] += 1
            else:
                pismena[znak] = 1

        nej = max(pismena.values())
        for znak in sorted(pismena.keys()):
            if znak.isalpha():
                done=print('{1:8d}| {0} | {2}'.format(znak, pismena[znak], 50 * pismena[znak] // nej * '*'))
    
    else:
        print('Špatná volba! Konec!')  


if prvnivolba==2:        
            def slovo (maxchars=10):
                vysledek = ''
                zacatek = randint(0,1)
                for _ in range(randint(1,maxchars)):
                    if _ % 2 == zacatek:
                        vysledek += choice(samohlasky)
                    else:
                        vysledek += choice(souhlasky)
                return vysledek

            def veta (maxwords=12):
                vysledek = ''
                for _ in range(randint(1,maxwords)):
                    vysledek += slovo() + ' '
                vysledek = vysledek[0:-1] + '.'
                return vysledek.capitalize()


            print (veta())
else:
    print('Špatná volba! Konec!')
