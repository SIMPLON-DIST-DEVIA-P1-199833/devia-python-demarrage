# EXO 1
char = 'z'
vowels = "aeiouAEIOU"
if char in vowels:
    print("True")
else:
    print("False")

# EXO 2
test_string = "coucou je suis debout"
if 'a' in test_string:
    print("True")
else:
    print("False")

# EXO 3
palindrome = "dskayaksd"
if palindrome == palindrome[::-1]:
    print("True")
else:
    print("False")

# EXO 3.1
palindrome = "akayaka"
for i in range(len(palindrome) // 2):
    if palindrome[i] != palindrome[- i - 1]:
        print("False")
        break
print(palindrome[0:4:-1])

# EXO 4 - Afficher les nombres pairs entre 1 et 20.
print("EXO 4")
print(*range(2,21,2))

# EXO 5 - Utiliser une boucle pour afficher chaque élément d'une liste.
print("\nEXO 5")
liste = ['t', 'e', 's', 't']
for i in range(len(liste)):
    print(liste[i])

# EXO 6 - Demander à l'utilisateur un nombre de 1 à 10 et afficher la table de multiplication.
'''
print("\nEXO 6")
try:
    mult = int(input("Choose a number between 1 and 10 so I can give you its multiplication table\n"))
    if mult >= 1 and mult <= 10:
        for i in range (1, mult + 1): 
            print(f"{mult} * {i} = {mult * i}")
    else:
        print("I said between 1 and 10 you dimwit")
except:
    print("lmao nice try")
'''

# EXO 7 - Utiliser `range()` pour afficher les nombres de 0 à 100 avec un pas de 10 - DEUX Syntaxes
print("\nEXO 7.0")
print(*range(0, 101, 10))

print("\nEXO 7.1")
nums = [i for i in range(0, 101, 10)]
print(nums)

# EXO 8 - Créer une boucle qui calcule la somme des nombres de 1 à 50.
print("\nEXO 8.0")
sum = 0
for i in range(1, 51):
    sum += i
print(sum)

# EXO 9 - Demander à l'utilisateur un nombre et continuer à demander tant que ce nombre est négatif.
'''
print("\nEXO 9.0")
keep_looping = 0
while keep_looping == 0:
    try:
        num = int(input("Give me any negative number (int):\n"))
        if num >= 0:
            print("Not negative")
            keep_looping = 1
    except:
        keep_looping = 1
        print("ValueError - Not a valid int")
'''
        
# EXO 10 - Date et Heure 
print("\nEXO 10.0")
import datetime as dt
maintenant = dt.datetime.now().strftime("It is now %I:%M %p on %B %d, %Y")
print(maintenant)

# EXO 11 - 
print("\nEXO 11.0")
import datetime as dt
from babel.dates import format_datetime, format_date, format_time, UTC, get_timezone

date_time = dt.datetime.now()
french = get_timezone('Europe/Paris')
date = format_date(date_time, format="EEEE dd MMMM yyyy", locale='fr_FR')
time = format_time(date_time, format="H:mm:ss", tzinfo=french, locale='fr_FR')
print(f"On est {date} et il est {time}")

