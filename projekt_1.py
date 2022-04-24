"""
projekt_1.py: Prvni projekt do Engeto Online Python Akademie

author: Láďa Bureš
email: ladislavb01@gmail.com
discord: Láďa#7333
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Uložené přihlašovací údaje
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
oddelovac = '-' * 40

# Požádání uživatele o zadání jména a hesla
username = input('Username: ')
password = input('Password: ')

# Ověří jestli zadané jméno a heslo souhlasí s uloženými údaji
if username in users.keys() and password in users.values():

    # ... pokud souhlasí, přivítá uživatele jménem
    print(oddelovac)
    print(f'Welcome to the app {username}. \nWe have 3 texts to be analyzed.')
    print(oddelovac)

    # ... pokud nesouhlasí, upozorní jej na chybné údaje a ukončí program
else:
    print('Unregistered user, terminating the program..')
    quit()

slova = []  # pocet vsech slov v textu
titlecase = []  # pocet slov zacinajicich velkym pismenem
lowerwords = [] # pocet slov malym pismem
upperwords = [] # pocet slov velkym pismem
cisla = []  # pocet cisel (ne cifer)
soucet = 0  # soucet všech čísel (ne cifer) v textu

# vyber z nabídky textu
vyber = input('Enter a number btw. 1 and 3 to select: ')

#pokud je zadana volba cislo a je ve stanovenem rozsahu
for x in vyber:
    if vyber.isnumeric():
        if int(vyber) in range(1, 4):
            text = TEXTS[int(vyber) - 1]
            # prida prvky do seznamu
            for slovo in text.split():
                bez_tecek = slovo.replace('.', '')
                bez_carek = bez_tecek.replace(',', '')
                slova.append(bez_carek)
                x = bez_carek[0]
                if x.isupper():
                    titlecase.append(x)
                elif bez_carek.islower():
                    lowerwords.append(bez_carek)
                elif bez_carek.isupper():
                    upperwords.append(bez_carek)
                elif bez_carek.isnumeric():
                    cisla.append(bez_carek)
                    soucet = soucet + int(bez_carek)
                else:
                    continue

        # pokud je volba cislo, ale mimo stanoveny rozsah
        else:
            print('Your choice is out of range, terminating the program..')
            quit()
    # pokud neni volba ciselna
    else:
        print("Your choice isn't numeric, terminating the program..")
        quit()

# seznam obsahujici delku slov a jejich pocet pro jednotlive delky slov
pocitani = {}
for x in slova:
    delka = len(x)
    if delka not in pocitani:
        pocitani[delka] = 1
    else:
        pocitani[delka] += 1

# vypis vsech pozadovanych vysledku
print(oddelovac)
print('There are', len(slova), 'words in the selected text.')
print('There are', len(titlecase), 'titlecase words.')
print('There are', len(lowerwords), 'lowercase words.')
print('There are', len(upperwords), 'uppercase words.')
print('There are', len(cisla), 'numeric strings.')
print('The sum of all the numbers ', soucet, '.')
print(oddelovac)

# graf obsahujici delky slov a jejich cetnost
sloupce = ['LEN', 'OCCURENCES', 'NR.']
print(f'|{sloupce[0]: ^5}| {sloupce[1]: ^25}| {sloupce[2]: ^4}|')
print(oddelovac)

for keys, values in sorted(pocitani.items()):

    print(f'| {keys: >3} | {"*" * values: <24} | {values: <3} |')

else:
    print(oddelovac)
