prix_unitaire = 12
quantite = 3
seuil_livraison = 50
tarif_livraison = 4

total = prix_unitaire * quantite

if total >= seuil_livraison:
    frais_livraison = 0
else:
    frais_livraison = tarif_livraison

montant_final = total + frais_livraison

print("Prix unitaire :", prix_unitaire)
print("Quantité :", quantite)
print("Total :", total)
print("Livraison :", frais_livraison)
print("À payer :", montant_final)
