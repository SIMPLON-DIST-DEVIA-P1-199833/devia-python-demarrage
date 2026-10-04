prix_unitaire = 12
seuil_livraison = 50
tarif_livraison = 4

for quantite in range(1, 6):
    total = prix_unitaire * quantite

    if total >= seuil_livraison:
        frais_livraison = 0
    else:
        frais_livraison = tarif_livraison

    montant_final = total + frais_livraison
    print("Quantité :", quantite, "— À payer :", montant_final)
