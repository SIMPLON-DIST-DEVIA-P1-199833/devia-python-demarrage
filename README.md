# Premiers pas Python — une commande qui évolue

**Objectif :** construire un programme avec des variables, une condition et une boucle.
**Prérequis :** aucun.

## Ouvrir l’environnement

Se connecter à GitHub, ouvrir [le dépôt](https://github.com/nimser/devia-python-demarrage), puis **Code → Codespaces → Create codespace on main**. Attendre l’ouverture de VS Code dans le navigateur.

Ouvrir `depart.py`. Le terminal se retrouve via **Terminal → New Terminal** dans le menu en haut à gauche. Depuis le dossier du fichier :

```sh
python3 depart.py
```

**Si l’accès bloque :** ouvrir [Basthon Console](https://console.basthon.fr/), copier `depart.py` dans l’éditeur puis cliquer sur **Exécuter**.

Pour chaque section : suivre la courte démo, faire l’exercice sur son propre fichier, puis vérifier et expliquer le résultat.

## 1. Variables et affichage

1. Lire `depart.py` et prédire sa sortie avant de l’exécuter.
2. Ajouter une variable `total` calculée à partir du prix unitaire et de la quantité.
3. Afficher un récapitulatif : prix unitaire, quantité et total.
4. Tester prix `12`, quantité `3`, puis prix `7`, quantité `5`. Prédire chaque résultat avant l’exécution.
5. Enregistrer sous `commande.py`. Expliquer une ligne modifiée à un binôme, puis relancer le fichier.

**Contrôle :** choisir une troisième quantité, prédire le total et vérifier avec le programme.
**Défi :** ajouter une variable `frais_fixes` de valeur `4` et afficher le montant final.

<details>
<summary>Indice — trouver le calcul</summary>

Quel calcul ferais-tu sur une calculatrice ? En Python, `*` multiplie deux valeurs. Utilise les noms des variables dans ce calcul.

</details>

<details>
<summary>Vérifier les totaux après l’essai</summary>

- Prix `12`, quantité `3` : total `36`.
- Prix `7`, quantité `5` : total `35`.
- Avec `4` de frais fixes : montants finaux `40` et `39`.

</details>

## 2. Conditions

La livraison coûte `4`. Elle est offerte quand le total des articles atteint `50`.

1. Repartir de `commande.py` et conserver le calcul du total des articles.
2. Utiliser `if` / `else` pour déterminer les frais de livraison.
3. Afficher le total des articles, les frais de livraison et le montant à payer.
4. Tester trois cas : prix `12`, quantité `4` ; prix `10`, quantité `5` ; prix `7`, quantité `8`.
5. Pour chaque cas, prédire la branche exécutée puis vérifier la sortie.

**Contrôle :** expliquer le comportement quand le total vaut exactement `50`.
**Défi :** placer le seuil et le tarif dans des variables, puis tester une autre règle.

<details>
<summary>Indice — comparer au seuil</summary>

`>=` signifie « supérieur ou égal ». Dans chaque branche, donne une valeur à la variable des frais de livraison. Calcule ensuite le montant à payer.

</details>

<details>
<summary>Vérifier les trois cas après l’essai</summary>

| Prix | Quantité | Articles | Livraison | À payer |
| --- | --- | --- | --- | --- |
| 12 | 4 | 48 | 4 | 52 |
| 10 | 5 | 50 | 0 | 50 |
| 7 | 8 | 56 | 0 | 56 |

</details>

## 3. Boucles

Après les petites démos, reprendre la même règle de livraison.

1. Fixer le prix unitaire à `12`.
2. Utiliser une boucle `for` pour parcourir les quantités de `1` à `5`.
3. À chaque tour, calculer le total des articles, les frais de livraison et le montant à payer.
4. Afficher une ligne par quantité, puis vérifier le nombre de lignes et les résultats.
5. Modifier la boucle pour parcourir les quantités de `1` à `8`.

**Contrôle :** expliquer ce qui change à chaque tour et quelles lignes sont répétées.
**Défi :** compter les quantités qui bénéficient de la livraison offerte.

<details>
<summary>Indice — les bornes et le bloc répété</summary>

`range(1, 6)` produit les entiers de `1` à `5`. L’indentation indique les instructions répétées. Place les calculs et l’affichage dans ce bloc.

</details>

<details>
<summary>Vérifier la boucle après l’essai</summary>

Pour les quantités de `1` à `5`, les montants à payer sont `16`, `28`, `40`, `52` et `60`.
Pour les quantités de `1` à `8`, quatre bénéficient de la livraison offerte.

</details>

## Expliquer et modifier

Présenter le programme à un binôme : rôle d’une variable, choix d’une branche et déroulement d’un tour de boucle. Chacun propose une nouvelle règle à l’autre, qui la teste sur son propre fichier.

**Livrable :** `commande.py`, avec des calculs vérifiés et une modification expliquée.
Les corrections `solution.py` et `solution_boucle.py` servent à comparer après l’essai personnel.

## Reprendre et explorer

Reprendre le programme, modifier une règle, puis retrouver et relancer le fichier. Découvrir l’interpréteur du projet et son environnement virtuel.

Choisir un parcours :

- **Pas à pas avec le formateur :** comprendre une variable, suivre sa valeur pendant l’exécution et distinguer mémoire et fichier enregistré.
- **Exploration personnelle :** choisir un blocage, écrire un petit exemple, chercher dans la documentation et noter ce qui a aidé.
- **Défi :** compter les livraisons offertes ou ajouter un budget et signaler les quantités accessibles.

**Point de sortie :** expliquer une chose comprise, montrer un blocage reproduit ou présenter un défi testé.

## Installer l’environnement local

1. Télécharger `commande.py` : clic droit → **Download** dans Codespaces, ou icône de téléchargement dans Basthon.
2. Installer Python et VS Code avec le parcours indiqué pour son système.
3. Ouvrir un dossier de projet local dans VS Code, y placer le fichier et installer l’extension **Python** de Microsoft.
4. Dans la palette de commandes, choisir **Python: Create Environment → Venv**, puis l’interpréteur Python installé.
5. Choisir cet environnement avec **Python: Select Interpreter**, puis lancer `commande.py` avec **Run Python File**.
6. Modifier une valeur, enregistrer et vérifier la nouvelle sortie.

**Si l’installation bloque :** poursuivre le lancement dans Codespaces et transmettre au formateur le message de blocage et l’étape concernée.

Déposer `commande.py` sur le Drive indiqué et envoyer le lien par Discord en MP. Terminer par **Stop codespace** depuis [la liste des Codespaces](https://github.com/codespaces).

Ressources : [tutoriel Python](https://docs.python.org/fr/3/tutorial/introduction.html), [Python](https://www.python.org/downloads/), [VS Code](https://code.visualstudio.com/download), [Python dans VS Code](https://code.visualstudio.com/docs/python/python-tutorial).
