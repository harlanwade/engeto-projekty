"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kryštof Karel
email: krystof.karel@gmail.com
discord: harlan.wade_63529
"""

'''
author =
'''
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

registred_users = {"bob": "123", "ann": "pass123",
                   "mike": "password123", "liz": "pass123"}

user = input("Zadej přihlašovací jméno: ")

password = input("Zadej heslo: ")

print(f"{'-' * 40}")

if registred_users.get(user) == password:
	print(f"""
Vítej {user}.
Jsou k dispozici {len(TEXTS)} texty k analýze.
{'-' * 40}
	""")
else:
	print("Neexistující uživatel.")
	exit()

vybrany_text = input(f"Vyber číslo mezi 1 a {len(TEXTS)}: ")

print(f"{'-' * 40}")
    
if vybrany_text.isnumeric() == False:
    print("Vybraný text není v nabídce.")
    exit()
    
vybrany_text = int(vybrany_text)
    
if vybrany_text not in range(1, len(TEXTS) + 1):
    print("Vybraný text není v nabídce.")
    exit()

text = TEXTS[vybrany_text - 1]

words = text.split()
number_of_words = len(words)
words_title = []
words_upper = []
words_lower = []
numbers = []

for word in words:
    if word.istitle():
        words_title.append(word)
    elif word.isupper():
        words_upper.append(word)
    elif word.isnumeric():
        numbers.append(int(word))
    else:
        words_lower.append(word)

number_of_words_title = len(words_title)
number_of_words_upper = len(words_upper)
number_of_words_lower = len(words_lower)
number_of_numbers = len(numbers)
sum_of_numbers = sum(numbers)
length_of_words = []
length_of_words_set = set()
length_of_words_count = []

for i, word in enumerate(words):
    words[i] = word.replace(",", "").replace(".", "")

for word in words:
    length_of_words.append(len(word))
    length_of_words_set.add(len(word))

for value in length_of_words_set:
    result = length_of_words.count(value)
    length_of_words_count.append(result)

length_of_words_set_sorted = sorted(list(length_of_words_set))

print(f"""
Ve vybraném textu je {number_of_words} slov.
Ve vybraném textu je {number_of_words_title} slov s velkým počátečním písmenem.
Ve vybraném textu je {number_of_words_upper} slov psaných velkými písmeny.
Ve vybraném textu je {number_of_words_lower} slov psaných malými písmeny.
Ve vybraném textu je {number_of_numbers} čísel.
Součet všech čísel ve vybraném textu je {sum_of_numbers}.
{'-' * 40}
LEN|{'OCCURENCES'.center(max(length_of_words_count))}|NR.
{'-' * 40}
""")

for i, item in enumerate(length_of_words_set_sorted, start=1):
    space = "  " if item < 10 else " "
    print(
    f"{space}{item}|{'*' * length_of_words_count[i - 1]}"
    f"{' ' * (max(length_of_words_count) - length_of_words_count[i - 1])}"
    f"|{length_of_words_count[i - 1]}"
    )
