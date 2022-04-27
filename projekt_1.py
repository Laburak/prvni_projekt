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

# vyber z nabídky textu
vyber = input('Enter a number btw. 1 and 3 to select: ')

# pokud je zadana volba cislo a je ve stanovenem rozsahu
for _ in vyber:
    if vyber.isnumeric() and int(vyber) in range(1, 4):
        continue
    else:
        print("Your choice is out of range, or your choice isn't numeric,  terminating the program..")
        quit()

clear_text = list()     # vsechna slova v textu
lowerwords = list()     # slova malym pismem
upperwords = list()     # slova velkym pismem
titlecase = list()
cisla = list()      # pocet cisel (ne cifer)
soucet = 0      # soucet všech čísel (ne cifer) v textu

# prida prvky do seznamu
text = TEXTS[int(vyber) - 1]
for slovo in text.split():
    clear_text.append(slovo.strip(",.:;!?"))

for word in clear_text:
    if word.islower():
        lowerwords.append(word)
    elif word.isupper():
        upperwords.append(word)
    elif word.istitle() and not word.isnumeric():
        titlecase.append(word)
    elif word.isnumeric():
        cisla.append(word)
        soucet = soucet + int(word)
    else:
        continue

# seznam obsahujici delku slov a jejich pocet pro jednotlive delky slov
pocitani = {}
for x in clear_text:
    delka = len(x)
    if delka not in pocitani:
        pocitani[delka] = 1
    else:
        pocitani[delka] += 1

# vypis vsech pozadovanych vysledku

print(oddelovac)
print('There are', len(clear_text), 'words in the selected text.')
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
