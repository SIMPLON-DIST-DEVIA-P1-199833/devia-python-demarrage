FRAIS_FIXES = 0
FORFAIT_LIVRAISON = 4
SEUIL_LIVRAISON_OFFERTE = 50

class Cart:
    def __init__(self, prix_unitaire, quantite):
        self.prix_unitaire = prix_unitaire
        self.quantite = quantite
        self.frais_fixes = FRAIS_FIXES
        self.seuil_livraison_offerte = SEUIL_LIVRAISON_OFFERTE
        self.forfait_livraison = FORFAIT_LIVRAISON

    def get_pre_total(self):
        return self.prix_unitaire * self.quantite

    def get_frais_livraison(self):
        if self.get_pre_total() >= self.seuil_livraison_offerte:
            return 0
        else:
            return self.forfait_livraison

    def get_total(self):
        return self.get_pre_total() + self.get_frais_livraison() + self.frais_fixes

    def __repr__(self):
        return str({"Prix unitaire": self.prix_unitaire, "Quantité": self.quantite, "Pré-total": self.get_pre_total(), "Frais fixes": self.frais_fixes, "Frais livraison": self.get_frais_livraison(), "Total": self.get_total()})


def test_cart_total(input_cart_values, expected_total):
    test_cart = Cart(input_cart_values[0], input_cart_values[1])
    print(test_cart)
    assert test_cart.get_total() == expected_total

def test_boucle_intervalle_quantite(prix_unitaire, quantite_start, quantite_end, expected_totals):
    lines = []
    for index, quantite in enumerate(range(quantite_start,quantite_end+1)):
        c = Cart(prix_unitaire, quantite)
        assert c.get_frais_livraison() == 0 if c.get_pre_total() >= 50 else c.forfait_livraison
        assert c.get_total() == expected_totals[index]
        lines.append(str(c))
    out = "\n".join(lines)
    print(out)
    assert len(out.split("\n")) == quantite_end

def main():
    global FRAIS_FIXES, FORFAIT_LIVRAISON, SEUIL_LIVRAISON_OFFERTE
    print("# 1. Variables et affichages")
    FRAIS_FIXES = 0
    FORFAIT_LIVRAISON = 0
    SEUIL_LIVRAISON_OFFERTE = 999
    print("""
    FRAIS_FIXES = 0
    FORFAIT_LIVRAISON = 0
    SEUIL_LIVRAISON_OFFERTE = 999
    """)

    test_cart_total([12, 3], 36)
    test_cart_total([7, 3], 21)
    test_cart_total([7, 5], 35)
    
    FRAIS_FIXES = 4
    print("""
    FRAIS_FIXES = 4
    """)
    test_cart_total([7,5], 35+FRAIS_FIXES)

    print("")
    print("# 2. Conditions")
    FRAIS_FIXES = 4
    FORFAIT_LIVRAISON = 4
    SEUIL_LIVRAISON_OFFERTE = 50
    print("""
    FRAIS_FIXES = 4
    FORFAIT_LIVRAISON = 4
    SEUIL_LIVRAISON_OFFERTE = 50
    """)

    test_cart_total([12, 4], 48+FRAIS_FIXES+FORFAIT_LIVRAISON)
    test_cart_total([10, 5], 50+FRAIS_FIXES+0)
    test_cart_total([7, 8], 7*8+FRAIS_FIXES+0)

    print("")
    print("# 3. Boucles")
    FRAIS_FIXES = 0
    print("## Quantités 1 à 5")
    test_boucle_intervalle_quantite(12, 1, 5, [16, 28, 40, 52, 60])

    print("## Quantités 1 à 8")
    test_boucle_intervalle_quantite(12, 1, 8, [16, 28, 40, 52, 60, 72, 84, 96])


if __name__ == "__main__":
    main()
