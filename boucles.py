prix_unitaire = 12
seuil = 50
tarif_livraison = 4
nombre_livraisons_offertes = 0

for quantite in range(1, 6):
    total = prix_unitaire * quantite

    if total >= seuil:
        frais_livraison = 0
        nombre_livraisons_offertes += 1
    else:
        frais_livraison = tarif_livraison

    montant_a_payer = total + frais_livraison

    print("Quantité :", quantite,
          "| Total :", total,
          "| Livraison :", frais_livraison,
          "| À payer :", montant_a_payer)

print("Nombre de quantités avec livraison offerte :",
      nombre_livraisons_offertes)