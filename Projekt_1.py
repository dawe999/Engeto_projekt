# první projekt do engeto Online Python Akademie

# author: David Čadek
# email: david.cadek@cezdistribuce.cz
# discord: coudy999


# Registrovaní uživatelé

user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Funkce pro analýzu textu
def analyze_text(text):
    words = text.split()
    num_words = len(words)
    num_capitalized_words = sum(1 for word in words if word.istitle())
    num_uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())          
    num_lowercase_words = sum(1 for word in words if word.islower())
    numbers = [int(word) for word in words if word.isdigit()]
    num_numbers = len(numbers)
    sum_numbers = sum(numbers)
    word_lengths = [len(word.strip(".,")) for word in words]

    return {
        "num_words": num_words,
        "num_capitalized_words": num_capitalized_words,
        "num_uppercase_words": num_uppercase_words,
        "num_lowercase_words": num_lowercase_words,
        "num_numbers": num_numbers,
        "sum_numbers": sum_numbers,
        "word_lengths": word_lengths
    }


# Sloupcový graf na délku slov
def print_word_lengths(word_lengths):                    
    length_counts = {}
    for length in word_lengths:
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1
    
    lengths = sorted(length_counts.keys())

    print("----------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    
    for length in lengths:
        occurrences = '*' * length_counts[length]
        print(f"{length:>3}|{occurrences:<20}|{length_counts[length]}")                                                              


# Vyžádání přihlašovacích údajů
username = input("Zadejte uživatelské jméno: ")
password = input("Zadejte heslo: ")

# Kontrola, zda je uživatel registrovaný
if username in user and user[username] == password:
    print(f"Vítejte, {username} :-)")
    
    # Umožnění analyzovat text
    try:
        text_number = int(input("Zadejte číslo textu, který chcete analyzovat: "))
        
# Texty pro analýzu
        texts = ['''
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
        
        if 1 <= text_number <= len(texts):
            text_to_analyze = texts[text_number - 1]
            result = analyze_text(text_to_analyze)
            print(f"Výsledky pro text číslo {text_number}:")
            print(f"Počet slov v textu {text_number}: {result['num_words']}")
            print(f"Počet slov začínajících velkým písmenem: {result['num_capitalized_words']}")
            print(f"Počet slov psaných velkými písmeny: {result['num_uppercase_words']}")
            print(f"Počet slov psaných malými písmeny: {result['num_lowercase_words']}")
            print(f"Počet čísel: {result['num_numbers']}")
            print(f"Suma všech čísel: {result['sum_numbers']}")

            # Sloupcový graf
            print_word_lengths(result['word_lengths'])

        else:
            print("Neplatné číslo textu. Program bude ukončen.")
    
    except ValueError:
        print("Neplatný vstup. Program bude ukončen.")
else:
    print("Neplatné uživatelské jméno nebo heslo. Program bude ukončen.")
