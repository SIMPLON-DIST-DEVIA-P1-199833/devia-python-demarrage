import math

prix_unitaire = 12
# quantite = 5
frais_livraison = 4
seuil = 50

# total = prix_unitaire * quantite 
# if total >= seuil:
#   frais_livraison = 0
# totalpayer = total + frais_livraison

for quantite in range(1, 9):
  total = prix_unitaire * quantite 
  if total >= seuil:
    frais_livraison = 0
  
  totalpayer = total + frais_livraison
  print("Total article :", total, "| Frais de livraison :", frais_livraison, "| Montant à payer :", totalpayer)

quantite_offerte = math.ceil(seuil / prix_unitaire)
print("Quantités minimum livraison offerte :", quantite_offerte)
  
  

# print("Quantité :", quantite)
# print("Prix unitaire :", prix_unitaire)
