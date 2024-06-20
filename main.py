"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Jeřábek
email: martinjer90@gmail.com
discord: blbec908874
"""
import sys
from texty import processed_texts #importuje texty.py
from collections import Counter

registrovani={"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

while True: #uživatel zadá jméno a heslo
  jmeno=input("Zadej své jméno:")
  heslo=input("Zadej své heslo:")

  if jmeno in registrovani and registrovani[jmeno] == heslo: #pokud se jméno a heslo shoduje s registrovanými, program pokračuje dál
    print("$ python projekt1.py\n", 
          "username: ", jmeno,"\n",
          "password: ", heslo,"\n",
          "-"*40,"\n",
          "Welcome to the app", jmeno,"\n",
          "We have 3 texts to be analyzed.\n",
          "-"*40)
    break
  if (jmeno in registrovani or heslo #pokud nesedí pouze jméno, nebo heslo, program se uživatele zeptá znovu
      in registrovani.values())and registrovani.get(jmeno) != heslo:
    print("Nesprávné jméno nebo heslo")
    continue
  else: #pokud nesedí ani jméno, ani heslo, program se ukončí
    print("$ python projekt1.\n",
          "username: ",jmeno,"\n",
          "password: ",heslo,"\n",
          "unregistered user, terminating the program..\n")
    sys.exit()

while True: #program vyžádá od uživatele výběr čísla textu, pokud je v rozmezí 1,2,3, program analyzuje konkrétní text
    cislo=int(input("Enter a number btw. 1 and 3 to select: "))-1
    if cislo in [0,1,2]:
        print("-"*40)
        print("There are",len(processed_texts[cislo]), "words in the selected text.")
        print("There are",sum(1 for word in processed_texts[cislo] if word.istitle()),
          "titlecase words.")
        print("There are",sum(1 for word in processed_texts[cislo] if word.isupper() 
                          and not any(char.isdigit() for char in word)),"uppercase words.")
        print("There are",sum(1 for word in processed_texts[cislo] if word.islower()),"lowercase words.")
        print("There are", sum(1 for word in processed_texts[cislo] if word.isnumeric()
                           and not any(char.isalpha() for char in word)),"numeric strings.")
        soucet=0
        for word in processed_texts[cislo]:
            if word.isdigit():
                soucet+=int(word)
        print("The sum of all the numbers:", soucet)
        print("-"*40)
        print(f'{"LEN":<2}|{" OCCURENCES":<12}|{"NR"}')
        print("-"*40)
    
        delky_slov = [len(slovo.strip('.,')) for slovo in processed_texts[cislo]]
        cetnosti = Counter(delky_slov)
        for delka, cetnost in sorted(cetnosti.items()):
            print(f'{delka:<2}|{"*" * cetnost:<12} |{cetnost}')
        print()
        break

    else: #pokud uživatel zadá jiné číslo, program se ukončí
        print("Zadal jsi špatné číslo. Ukončuji program.")
        sys.exit()