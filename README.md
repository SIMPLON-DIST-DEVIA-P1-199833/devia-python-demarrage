# Premiers pas Python — petit calcul de commande

**Objectif :** modifier, expliquer, enregistrer et relancer un script Python.
**Prérequis :** aucun en programmation ; savoir ouvrir un lien et enregistrer un fichier.
**Durée :** atelier de 75 minutes, après une démonstration guidée.
**Données :** prix et quantités fictifs, en nombres entiers.

## Ouvrir l’environnement

Dépôt pédagogique privé : [nimser/devia-python-demarrage](https://github.com/nimser/devia-python-demarrage). Le formateur doit autoriser l’accès au compte apprenant avant mardi ; un compte GitHub seul ne donne pas accès au dépôt. Se connecter au compte créé lundi, ouvrir **Code → Codespaces → Create codespace on main** et utiliser une machine à **2 cœurs**. Attendre l’ouverture de VS Code dans le navigateur. Aucune commande Git n’est demandée.

Ouvrir `depart.py`, puis **Terminal → New Terminal**. Dans le dossier contenant le fichier :

```sh
python3 --version
python3 depart.py
```

Sortie attendue du second appel :

```text
Prix unitaire : 12
Quantité : 3
```

**Si l’accès bloque :** ouvrir [Basthon Console](https://console.basthon.fr/), copier `depart.py` dans l’éditeur puis cliquer sur **Exécuter**. Aucun compte ni installation. Basthon permet de faire le calcul, pas les manipulations de terminal ou de `venv`.

## Consignes

1. Lire le code et prédire la sortie avant de l’exécuter.
2. Ajouter une variable `total` qui multiplie le prix par la quantité, puis afficher ce total.
3. Enregistrer et exécuter. Avec un prix de `12` et une quantité de `3`, le total attendu est `36`.
4. Remplacer le prix par `7` et la quantité par `5`. Avant l’exécution, annoncer le total attendu : `35`.
5. Expliquer à un binôme ce qui change et ce qui reste identique. Chaque personne modifie son propre script.
6. Revenir au premier jeu de valeurs. Enregistrer sous `commande.py`, puis relancer.

**Résultat attendu :** un fichier `commande.py` qui affiche prix, quantité et total, correct sur les deux jeux de valeurs. Montrer sa relance et expliquer une ligne modifiée.

## Enregistrer et remettre

Dans Codespaces, télécharger `commande.py` depuis l’explorateur de fichiers (**clic droit → Download**). Dans Basthon, utiliser l’icône de téléchargement du code Python. Vérifier que le fichier est présent dans les téléchargements et porte l’extension `.py`.

Déposer le fichier sur le Drive indiqué par le formateur, puis transmettre le lien par Discord en MP, sans notification par courriel. Aucun dépôt Git demandé. Dans Codespaces, terminer par **Stop codespace** depuis [la liste des Codespaces](https://github.com/codespaces).

## Aide graduée et défi

- Indice 1 : `*` représente une multiplication.
- Indice 2 : `total = prix_unitaire * quantite` calcule le total.
- Indice 3 : `print("Total :", total)` l’affiche.
- Défi : ajouter des frais fixes de `4` ; vérifier un montant final de `40` puis de `39`.

La correction `solution.py` est à ouvrir après l’essai personnel. Ressource : [nombres et variables dans le tutoriel Python](https://docs.python.org/fr/3/tutorial/introduction.html#using-python-as-a-calculator).
