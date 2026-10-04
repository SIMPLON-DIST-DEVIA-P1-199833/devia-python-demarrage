# Premiers pas Python — petit calcul de commande

**Objectif :** modifier, expliquer, enregistrer et relancer un script Python.
**Prérequis :** aucun.
**Durée :** ~45mn


## Ouvrir l’environnement

Dépôt pédagogique privé : [nimser/devia-python-demarrage](https://github.com/nimser/devia-python-demarrage). Se connecter au compte créé lundi, ouvrir **Code → Codespaces → Create codespace on main**. Attendre l’ouverture de VS Code dans le navigateur. 

Ouvrir `depart.py`.

Note: Si vous fermez le terminal par erreur, vous pouvez le retrouver via **Terminal → New Terminal** dans le menu en haut à gauche.

Dans le dossier contenant le fichier :

```sh
python3 --version
python3 depart.py
```

Sortie attendue du second appel :

```text
Prix unitaire : 12
Quantité : 3
```

**Si l’accès bloque :** ouvrir [Basthon Console](https://console.basthon.fr/), copier `depart.py` dans l’éditeur puis cliquer sur **Exécuter**.

## Consignes

1. Lire le code et prédire la sortie avant de l’exécuter.
2. Ajouter une variable `total` qui multiplie le prix par la quantité, puis afficher ce total.
3. Avec un prix de `12` et une quantité de `3`, prédire le total, puis enregistrer et exécuter.
4. Remplacer le prix par `7` et la quantité par `5`. Avant l’exécution, annoncer le total attendu.
5. Expliquer à un binôme ce qui change et ce qui reste identique. Chaque personne modifie son propre script.
6. Revenir au premier jeu de valeurs. Enregistrer sous `commande.py`, puis relancer.

<details>
<summary>Vérifier les totaux après l’essai</summary>

- Prix `12`, quantité `3` : total `36`.
- Prix `7`, quantité `5` : total `35`.

</details>

**Résultat attendu :** un fichier `commande.py` qui affiche prix, quantité et total, correct sur les deux jeux de valeurs. Montrer sa relance et expliquer une ligne modifiée.

## Enregistrer et remettre

Dans Codespaces, télécharger `commande.py` depuis l’explorateur de fichiers (**clic droit → Download**). Dans Basthon, utiliser l’icône de téléchargement du code Python. Vérifier que le fichier est présent dans les téléchargements et porte l’extension `.py`.

Déposer le fichier sur le Drive indiqué par le formateur, puis transmettre le lien par Discord en MP, sans notification par courriel. Aucun dépôt Git demandé. Dans Codespaces, terminer par **Stop codespace** depuis [la liste des Codespaces](https://github.com/codespaces).

## Aide graduée et défi

<details>
<summary>Indice 1 — l’opérateur</summary>

`*` représente une multiplication.

</details>

<details>
<summary>Indice 2 — calculer le total</summary>

`total = prix_unitaire * quantite` calcule le total.

</details>

<details>
<summary>Indice 3 — afficher le total</summary>

`print("Total :", total)` l’affiche.

</details>

**Défi :** ajouter des frais fixes de `4` ; prédire puis vérifier le montant final pour les deux jeux de valeurs.

<details>
<summary>Vérifier les montants du défi après l’essai</summary>

- Prix `12`, quantité `3` : montant final `40`.
- Prix `7`, quantité `5` : montant final `39`.

</details>

La correction `solution.py` est à ouvrir après l’essai personnel. Ressource : [nombres et variables dans le tutoriel Python](https://docs.python.org/fr/3/tutorial/introduction.html#using-python-as-a-calculator).
