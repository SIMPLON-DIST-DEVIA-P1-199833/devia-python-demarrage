# # EXERCICE 1

# prix_unitaire = 7
# quantite = 5
# frais_fixes = 4
# total = prix_unitaire * quantite
# montant_final = total + frais_fixes

# print("Prix unitaire :", prix_unitaire)
# print("Quantité :", quantite)
# print("Total :", total)
# print("Frais fixes :", frais_fixes)
# print("Montant final :", montant_final)

# # Exo 2

# prix_unitaire = 10
# quantite = 5
# min_commande = 50
# total = prix_unitaire * quantite

# if total >= min_commande:
#     frais_livraison = 0
# else: 
#     frais_livraison = 4
    
# montant_final = total + frais_livraison

# print("Total articles :", total)
# print("Frais de livraison :", frais_livraison)
# print("Montant final :", montant_final)

# Exo 3

prix_unitaire = 12
min_commande = 50
nb_livraison_offerte = 0

for qté in range(1,8):
    total = prix_unitaire * qté
    
    if total >= min_commande:
        frais_livraison = 0
        nb_livraison_offerte += 1
    else: 
        frais_livraison = 4
            
    montant_final = total + frais_livraison

    print("Quantité :", qté)
    print("Total :", total)
    print("Frais de livraison :", frais_livraison)
    print("Montant final :", montant_final)
    print("-----")
    
print("Nombre de livraison offerte :", nb_livraison_offerte)