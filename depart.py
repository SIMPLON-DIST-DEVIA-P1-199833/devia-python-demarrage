# 1. Variables et affichage

frais_fixes = 4

#Exemple 1
prix_unitaire = 12
quantite = 3
total = prix_unitaire * quantite
montant_final = total + frais_fixes
print("1. Variables et affichage")

print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)
print("Montant Final :", montant_final)

#Exemple 2
prix_unitaire = 7
quantite = 5
total = prix_unitaire * quantite
montant_final = total + frais_fixes

print("\nPrix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)
print("Montant Final :", montant_final)

#Exemple 3
prix_unitaire = 2
quantite = 12
total = prix_unitaire * quantite
montant_final = total + frais_fixes

print("\nPrix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)
print("Montant Final :", montant_final)

# 2. Conditions
print("\n2. Conditions")

#Exemple 1
prix_unitaire = 12
quantite = 4
total = prix_unitaire * quantite
frais_livraison = 4
if total >= 50:
    frais_livraison = 0
montant_final = total + frais_livraison

print("Total :", total)
print("Frais Livraison:", frais_livraison)
print("Montant Final :", montant_final)

#Exemple 2
prix_unitaire = 10
quantite = 5
total = prix_unitaire * quantite
frais_livraison = 4
if total >= 50:
    frais_livraison = 0
montant_final = total + frais_livraison

print("\nTotal :", total)
print("Frais Livraison:", frais_livraison)
print("Montant Final :", montant_final)

#Exemple 3
prix_unitaire = 7
quantite = 8
total = prix_unitaire * quantite
frais_livraison = 4
if total >= 50:
    frais_livraison = 0
montant_final = total + frais_livraison

print("\nTotal :", total)
print("Frais Livraison:", frais_livraison)
print("Montant Final :", montant_final)

#Exemple 4
prix_unitaire = 8
quantite = 13
total = prix_unitaire * quantite
seuil_livraison_offert = 100
frais_livraison = 10
if total >= seuil_livraison_offert:
    frais_livraison = 0
montant_final = total + frais_livraison

print("\nTotal :", total)
print("Frais Livraison:", frais_livraison)
print("Montant Final :", montant_final)

# 2. Boucles
print("\n3. Boucles")

#Exemple 1
prix_unitaire = 12

for i in range(1, 6):
    total = prix_unitaire * i
    if total >= 50:
        frais_livraison = 0
    else:
        frais_livraison = 4
    montant_final = total + frais_livraison
    print("Quantite:", i, "| Montal Final:", montant_final)

#Exemple 2
prix_unitaire = 12
livrasons_offertes = 0

print("")
for i in range(1, 9):
    total = prix_unitaire * i
    if total >= 50:
        frais_livraison = 0
        livrasons_offertes += 1
    else:
        frais_livraison = 4
    montant_final = total + frais_livraison
    print("Quantite:", i, "| Montal Final:", montant_final)
print("Livraisons Offertes:", livrasons_offertes)

# Exercice 1
prenom = str("Gaetan")
age = int(29)
taille = float(1.75)

print("EXERCICE 1")
print("Prenom:", prenom)
print("Age:", age)
print("Taille:", taille)
phrase = "Je m'appelle {}, j'ai {} et je mesure {}m.".format(prenom, age, taille)
print(phrase)

# Exercice 2
print("\nEXERCICE 2")
valeur_str = "42"
print(type(valeur_str))
valeur_int = int(valeur_str)
print(valeur_int, type(valeur_int))
valeur_float = float(valeur_int)
print(valeur_float, type(valeur_float))

# Exercice 3
print("\nEXERCICE 3")
n = 12
if n == 0:
    print("n is zero")
elif n > 0:
    print("n is positive")
else:
    print("n is negative")

# Exercice 4
print("\nEXERCICE 4")
string = "this is a test"
empty_string = ""
print("string:", string)
print("empty string:", empty_string)
print("is 'string' empty ?", bool(string))
print("is 'empty_string' empty ?", bool(empty_string))

# Exercice 5
print("\nEXERCICE 5")

password = input('what is your password - hint, it is admin\n')
if password == "admin":
    print('insane, you can read')
else:
    print('unlucky reading comprehension')