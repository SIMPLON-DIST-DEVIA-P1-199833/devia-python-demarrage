# Premiers pas Python — guide formateur

## Préparer la séance

- Vérifier les accès apprenants au dépôt, puis tester Codespaces à 2 cœurs : lancement, téléchargement, arrêt et reprise.
- Préparer les liens Discord, le dossier Drive de remise et une copie de `depart.py` pour [Basthon](https://console.basthon.fr/).
- Relever les OS et droits d’installation ; tester les parcours Python / VS Code / extension Python / Venv sur ces systèmes.
- Prévoir des salles visio pour les trois parcours de consolidation et afficher leurs consignes avant de rejoindre le groupe accompagné.

## Démo, pratique, vérification

| Animation | Contrôle |
| --- | --- |
| Variables : démo, section 1, comparaison. | Nouvelle quantité : prédiction, exécution, explication. |
| Conditions : démo, section 2, vérification. | Sous le seuil, au seuil et au-dessus ; branche expliquée. |
| Boucles : trois démos, chacune suivie de pratique, puis intégration de la livraison. | Nombre de tours, borne finale et indentation expliqués. |
| Explication en binômes, modification individuelle, retour collectif. | Variable, condition et tour de boucle expliqués. |

Avant chaque exécution, demander une prédiction dans le chat. Faire écrire et modifier leur propre fichier ; afficher les corrections après l’essai. Si les variables restent fragiles, les consolider avant d’aborder les boucles.

### Variables — `demos/variables.py`

Utiliser les places disponibles dans une salle. Demander la sortie, puis changer `places_occupees` de `18` à `23`. Faire distinguer le nom, la valeur et le calcul. Le changement prend effet à la prochaine exécution du script.

### Conditions — `demos/conditions.py`

Utiliser la température : `22`, `25`, puis `28`. Faire verbaliser la comparaison et la branche exécutée. Montrer `:` et l’indentation. Revenir sur le cas exactement au seuil avant la pratique sur la livraison.

### Boucles — `demos/boucles.py`

Montrer un bloc à la fois : répétition de « Bonjour », numéro du passage, puis places restantes. Avant chaque bloc, faire prédire le nombre de lignes et les valeurs successives. Faire varier une borne avant de passer au bloc suivant.

### Corrections de l’atelier

- Section 1 : `total = prix_unitaire * quantite`, puis `print("Total :", total)` ; totaux `36` et `35`.
- Section 2 : `solution.py` ; cas articles/livraison/montant : `48/4/52`, `50/0/50`, `56/0/56`.
- Section 3 : `solution_boucle.py` ; montants `16`, `28`, `40`, `52`, `60`. De 1 à 8, quatre quantités ont la livraison offerte.
- Défi compteur : initialiser à `0` avant la boucle, ajouter `1` dans la branche livraison offerte, afficher après la boucle.

## Réinvestir et comprendre l’environnement

Demander une autre règle de livraison ; chacun la teste et explique un cas limite. Relever les difficultés avant la consolidation.

Retrouver `commande.py`, le télécharger, le rouvrir et le relancer. Montrer éditeur, terminal et interpréteur, puis créer un environnement virtuel dans Codespaces. Préparer le dossier et les téléchargements de l’installation locale.

Depuis le dossier du projet dans Linux / Codespaces :

```sh
python3 --version
python3 -m venv .venv
.venv/bin/python --version
.venv/bin/python commande.py
.venv/bin/python -m pip --version
```

`python -m pip` utilise pip associé à cet interpréteur. Le dossier `.venv` contient l’interpréteur du projet et ses dépendances ; le code de l’atelier utilise la bibliothèque standard. Les chemins ci-dessus correspondent à Linux.

## Trois parcours parallèles

Démarrer le parcours choisi, puis partager une explication, une friction ou un résultat. Chacun peut changer de parcours selon ses besoins.

### Avec NW — les variables, pas à pas

Utiliser `demos/memoire.py`, ligne par ligne. Dessiner des étiquettes reliées aux valeurs :

1. `nombre = 10` : le nom `nombre` est associé à un objet entier de valeur `10` en mémoire.
2. `copie = nombre` : le nom `copie` désigne le même objet entier à ce moment.
3. `nombre = nombre + 5` : lire la valeur associée à `nombre`, calculer `15`, puis associer `nombre` au résultat. `copie` reste associé à `10`.
4. `print(nombre)` : lire la valeur et l’afficher. Demander les deux sorties avant d’exécuter.

L’image de l’étiquette est un modèle pour les noms Python. Les nombres entiers sont immuables ; le comportement de cet exemple sera à distinguer de celui des listes mutables. Les données de l’exécution sont en mémoire vive ; enregistrer le `.py` conserve les instructions sur un stockage durable. Relancer exécute ces instructions depuis le début.

Faire tracer un nouvel exemple à la main avant de le lancer. Contrôle : expliquer pourquoi `copie` affiche encore `10`, et ce que conserve le fichier enregistré.

### Autonomie — une friction personnelle

Choisir une difficulté : indentation, bornes de `range`, comparaison, fichier introuvable ou erreur de nom. Écrire le plus petit exemple qui reproduit le problème, prédire le résultat, consulter la documentation et essayer une modification. À la sortie : montrer l’exemple et ce qui a permis d’avancer, ou la question encore ouverte.

### Autonomie — défis

- Compter les quantités de 1 à 8 bénéficiant de la livraison offerte ; expliquer où le compteur est initialisé et modifié.
- Ajouter un budget de `80` et afficher quelles quantités restent accessibles ; tester le cas exactement au budget.

À la sortie : montrer les cas testés et expliquer une ligne. NW accompagne le pas à pas ; les autres parcours utilisent les consignes écrites et une comparaison en binômes.

## Installer et vérifier sur son poste

- Installer Python et VS Code avec la notice de l’OS ; ouvrir le dossier local contenant `commande.py` et installer l’extension Python de Microsoft.
- **Python: Create Environment → Venv**, choisir Python, puis **Python: Select Interpreter** et lancer le fichier.
- Modifier une valeur, enregistrer et relancer ; montrer le résultat avec l’interpréteur du projet.
- Déposer le `.py` sur Drive, transmettre le lien par Discord en MP, météo finale et arrêt du Codespace.

Objectif : Python, VS Code et un environnement virtuel utilisables localement. Un poste bloqué continue dans Codespaces ; relever l’étape et le message nécessaires à la reprise. Préparer les téléchargements et droits avant l’installation.

Ressources : [Python](https://www.python.org/downloads/), [VS Code](https://code.visualstudio.com/download), [parcours officiel Python / VS Code](https://code.visualstudio.com/docs/python/python-tutorial), [venv](https://docs.python.org/fr/3.13/library/venv.html).

## Points Python à surveiller

- `=` associe un nom à une valeur ; `==` compare deux valeurs.
- `print` affiche les arguments séparés par des espaces, puis un retour à la ligne.
- Un bloc commence après `:` et se reconnaît à son indentation ; `else` s’aligne sur `if`.
- La borne finale de `range` est exclue ; les calculs dans la boucle sont refaits à chaque tour.
- Lire la dernière ligne d’une erreur, repérer le fichier et la ligne, corriger puis relancer.

## Contrôles techniques

```sh
python3 -m unittest discover -s tests -v
```

Les tests couvrent les démos, les cas de livraison, les bornes de boucle, le compteur et l’exécution dans un environnement virtuel. La vérification locale Linux ne valide pas une installation Windows/macOS ni le parcours complet Codespaces avec les droits apprenant. Ces parcours font partie de la préparation technique avant diffusion.
