# Kit Python — préparation et contrôles formateur

## Préparer Codespaces

Dépôt dédié privé : [nimser/devia-python-demarrage](https://github.com/nimser/devia-python-demarrage), créé à la demande de NW. NW prévoit son transfert vers WCS ou Simplon après confirmation avec Julien ; ne pas modifier l’organisation ou la visibilité automatiquement. Le dépôt ne contient pas les documents internes DevIA.

1. Maintenir le **contenu** du kit à la racine du dépôt dédié, dont `.devcontainer/devcontainer.json` et `.gitignore`. Le kit du dépôt DevIA en est la source de préparation.
2. Vérifier les droits d’accès des apprenants ; un compte GitHub seul ne donne pas accès à un dépôt privé. Ne pas publier le dépôt DevIA ni ses documents internes.
3. Tester avec un compte disposant seulement des droits apprenant : machine 2 cœurs, démarrage, ouverture du fichier, terminal, exécution, téléchargement, arrêt puis reprise.
4. Transmettre le lien par Discord. Faire vérifier la connexion au compte créé lundi ; ne jamais recueillir mots de passe ou codes d’authentification.

Configuration : image Microsoft Python 3.13 sur Debian Bookworm, utilisateur non-root `vscode`, extensions Python/Pylance. Aucun serveur, port exposé ou dépendance externe pour l’atelier. L’activation automatique de l’environnement est désactivée pour que l’interpréteur utilisé soit explicite.

## Quota et sauvegarde

[GitHub Free personnel](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) : 120 heures-cœur/mois, soit 60 heures sur 2 cœurs, et 15 Go-mois de stockage. Vérifier le quota disponible, ne pas demander de carte bancaire. Les organisations n’ont pas ce quota gratuit. Un arrêt réduit le calcul consommé, mais le stockage reste compté tant que le Codespace existe.

Faire télécharger le `.py` avant l’arrêt ; ce téléchargement est la preuve de sauvegarde hors Codespaces. Ne supprimer un Codespace qu’après sauvegarde vérifiée par son propriétaire. Ne pas compter sur le quota gratuit pour toute la formation.

## Démonstration guidée après-midi

Le premier script n’exige ni environnement virtuel ni paquet tiers. Utiliser Codespaces pour une démonstration Linux commune ; accompagner les installations locales uniquement avec une notice testée pour l’OS constaté lundi.

```sh
python3 --version
python3 -m venv .venv
.venv/bin/python --version
.venv/bin/python depart.py
.venv/bin/python -m pip --version
```

Ces chemins concernent Linux/Codespaces, pas Windows. Sous Windows, utiliser `py -3` pour créer l’environnement, puis `.venv\Scripts\python.exe` pour le lancer, après vérification sur un poste Windows. Ne pas imposer l’activation du shell ; appeler directement l’interpréteur évite de mêler plusieurs syntaxes.

Montrer `python -m pip` : il associe pip à cet interpréteur. Ne pas installer de paquet pour le seul principe d’utiliser pip. Expliquer : éditeur = texte ; interpréteur = exécution ; terminal = commandes ; environnement virtuel = dépendances isolées du projet.

## Points délicats pour NW

- Python n’a pas `let`/`const`, ni accolades ou point-virgule à ajouter aux exemples.
- `=` affecte une valeur ; le code s’exécute dans l’ordre. Modifier une valeur impose de relancer le script.
- Les noms sont sensibles à la casse ; `Quantite` et `quantite` diffèrent.
- `print` accepte plusieurs arguments séparés par des virgules ; il ajoute espaces et retour à la ligne.
- Lire la dernière ligne d’une trace d’erreur, puis repérer le fichier et la ligne. Provoquer `print(totla)` pour une `NameError`, puis corriger.
- Ne pas introduire conditions, boucles ou fonctions avant d’avoir vérifié modification et compréhension des exemples simples.

## Repli et contrôle

Après cinq minutes de blocage d’accès, passer sur [Basthon Console](https://console.basthon.fr/) et continuer le même calcul. Prévoir la copie de `depart.py` dans le message Discord si le dépôt n’est pas accessible. Faire télécharger le code : le stockage du navigateur n’est pas une remise.

Accompagnement : un binôme verbalise pendant que chacun manipule ; NW dépanne un sous-groupe à la fois. Si les variables restent fragiles, réduire à un calcul et deux `print`. Si le groupe avance, ajouter les frais fixes, puis une faute de nom à diagnostiquer.

Contrôle individuel : prédire `36`, puis `35`, obtenir les deux sorties, expliquer la multiplication, relancer le fichier sauvegardé. Défi : `40`, puis `39`. La solution utilise seulement des entiers ; ne pas ouvrir la question des arrondis monétaires à ce stade.

## Vérifications techniques

```sh
python3 -m unittest discover -s tests -v
```

Vérification du 3 octobre 2026 : six tests réussis sur Python 3.13.12, dont les deux jeux de valeurs, la faute de nom, `venv`, pip et la présence du devcontainer. Dans Basthon Console (Python 3.12.1), les résultats 36 et 35 et l’export du script ont été vérifiés dans le navigateur. Le manifeste de l’image Microsoft Python 3.13 Bookworm répond HTTP 200.

Ces contrôles ne prouvent pas le démarrage réel dans Codespaces. Le parcours Codespaces doit être validé avant diffusion ; aucune installation Windows n’est déclarée testée.
