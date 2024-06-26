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

while True: #program vyžádá od uživatele výběr čísla textu, pokud je v rozmezí, program analyzuje konkrétní text
  try:
    cislo=int(input("Enter a number btw. 1 and 3 to select: "))-1
    if 0 <= cislo < len(processed_texts):
      selected_text = processed_texts[cislo]
      print("-"*40)
      pocet_slov = len(selected_text)
      titlecase_count = 0
      uppercase_count = 0
      lowercase_count = 0
      numeric_count = 0
      soucet = 0
      
      for word in selected_text:
                if word[0].isalpha() and word[0].isupper():                
                    titlecase_count += 1
                if word.isupper() and not any(char.isdigit() for char in word):
                    uppercase_count += 1
                if word.islower():
                    lowercase_count += 1
                if word.isnumeric() and not any(char.isalpha() for char in word):
                    numeric_count += 1
                if word.isdigit():
                    soucet += int(word)
      
      
      print("There are", pocet_slov, "words in the selected text.")
      print("There are", titlecase_count, "titlecase words.")
      print("There are", uppercase_count, "uppercase words.")
      print("There are", lowercase_count, "lowercase words.")
      print("There are", numeric_count, "numeric strings.")
      print("The sum of all the numbers:", soucet)
      print("-" * 40)
      print(f'{"LEN":<3}|{" OCCURRENCES":<13}|{"NR"}')
      print("-" * 40)
      
      delky_slov = [len(slovo.strip('.,')) for slovo in processed_texts[cislo]]
      cetnosti = Counter(delky_slov)
      for delka, cetnost in sorted(cetnosti.items()):
        print(f'{delka:<3}|{"*" * cetnost:<13} |{cetnost}',end="")
        print()
        continue
      break
      
      

    else: #pokud uživatel zadá jiné číslo, program se ukončí
        print("Zadal jsi špatné číslo. Ukončuji program.")
        sys.exit()
  except ValueError:#pokud zadá uživatel něco jiného, než číslo, taky se ukončí
    print("Zadal jsi neplatný vstup. Ukončuji program.")
    sys.exit()