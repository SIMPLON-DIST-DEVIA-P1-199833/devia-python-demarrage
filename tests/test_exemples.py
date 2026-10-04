import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PremiersPasTests(unittest.TestCase):
    def executer(self, nom, remplacements=()):
        source = (ROOT / nom).read_text(encoding="utf-8")
        for avant, apres in remplacements:
            self.assertEqual(source.count(avant), 1, avant)
            source = source.replace(avant, apres)
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            exec(compile(source, nom, "exec"), {})
        return sortie.getvalue()

    def test_depart(self):
        self.assertEqual(self.executer("depart.py"), "Prix unitaire : 12\nQuantité : 3\n")

    def test_solution(self):
        self.assertEqual(
            self.executer("solution.py"),
            "Prix unitaire : 12\nQuantité : 3\nTotal : 36\nLivraison : 4\nÀ payer : 40\n",
        )

    def test_second_jeu(self):
        self.assertEqual(
            self.executer("solution.py", (("prix_unitaire = 12", "prix_unitaire = 7"), ("quantite = 3", "quantite = 5"))),
            "Prix unitaire : 7\nQuantité : 5\nTotal : 35\nLivraison : 4\nÀ payer : 39\n",
        )

    def test_livraison_sous_au_et_dessus_du_seuil(self):
        for prix, quantite, total, livraison, montant in [(12, 4, 48, 4, 52), (10, 5, 50, 0, 50), (7, 8, 56, 0, 56)]:
            with self.subTest(prix=prix, quantite=quantite):
                self.assertEqual(
                    self.executer("solution.py", (("prix_unitaire = 12", f"prix_unitaire = {prix}"), ("quantite = 3", f"quantite = {quantite}"))),
                    f"Prix unitaire : {prix}\nQuantité : {quantite}\nTotal : {total}\nLivraison : {livraison}\nÀ payer : {montant}\n",
                )

    def test_regle_modifiee(self):
        self.assertTrue(self.executer("solution.py", (("seuil_livraison = 50", "seuil_livraison = 30"),)).endswith("Livraison : 0\nÀ payer : 36\n"))

    def test_boucle(self):
        lignes = self.executer("solution_boucle.py").splitlines()
        self.assertEqual(lignes, [f"Quantité : {q} — À payer : {m}" for q, m in enumerate([16, 28, 40, 52, 60], start=1)])

    def test_boucle_etendue(self):
        lignes = self.executer("solution_boucle.py", (("range(1, 6)", "range(1, 9)"),)).splitlines()
        self.assertEqual(lignes, [f"Quantité : {q} — À payer : {m}" for q, m in enumerate([16, 28, 40, 52, 60, 72, 84, 96], start=1)])

    def test_defi_compteur(self):
        source = (ROOT / "solution_boucle.py").read_text(encoding="utf-8")
        source = "livraisons_offertes = 0\n" + source.replace("range(1, 6)", "range(1, 9)").replace("        frais_livraison = 0", "        frais_livraison = 0\n        livraisons_offertes = livraisons_offertes + 1")
        valeurs = {}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(source, "defi", "exec"), valeurs)
        self.assertEqual(valeurs["livraisons_offertes"], 4)

    def test_demo_variables(self):
        self.assertEqual(self.executer("demos/variables.py"), "Places restantes : 12\n")
        self.assertEqual(self.executer("demos/variables.py", (("places_occupees = 18", "places_occupees = 23"),)), "Places restantes : 7\n")

    def test_demo_conditions(self):
        for temperature, message in [(22, "Garder la fenêtre fermée"), (25, "Ouvrir la fenêtre"), (28, "Ouvrir la fenêtre")]:
            with self.subTest(temperature=temperature):
                self.assertEqual(self.executer("demos/conditions.py", (("temperature = 22", f"temperature = {temperature}"),)), message + "\n")

    def test_demo_boucles(self):
        self.assertEqual(self.executer("demos/boucles.py").splitlines(), ["Bonjour"] * 3 + ["Passage : 1", "Passage : 2", "Passage : 3", "Passage : 1 — Places restantes : 26", "Passage : 2 — Places restantes : 22", "Passage : 3 — Places restantes : 18"])

    def test_demo_memoire(self):
        self.assertEqual(self.executer("demos/memoire.py"), "Nombre : 15\nCopie : 10\n")

    def test_faute_de_nom(self):
        with self.assertRaises(NameError):
            self.executer("solution.py", (('print("Total :", total)', "print(totla)"),))

    def test_devcontainer(self):
        config = json.loads((ROOT / ".devcontainer/devcontainer.json").read_text())
        self.assertEqual(config["image"], "mcr.microsoft.com/devcontainers/python:3.13-bookworm")
        self.assertEqual(config["remoteUser"], "vscode")
        self.assertEqual(config["hostRequirements"]["cpus"], 2)
        self.assertFalse(config["customizations"]["vscode"]["settings"]["python.terminal.activateEnvironment"])

    def test_venv_et_pip(self):
        with tempfile.TemporaryDirectory() as dossier:
            env = Path(dossier) / ".venv"
            subprocess.run([sys.executable, "-m", "venv", str(env)], check=True)
            python = env / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
            sortie = subprocess.run([str(python), str(ROOT / "solution.py")], check=True, capture_output=True, text=True)
            self.assertEqual(sortie.stdout, self.executer("solution.py"))
            pip = subprocess.run([str(python), "-m", "pip", "--version"], check=True, capture_output=True, text=True)
            self.assertIn(str(env), pip.stdout)

    def test_aides_et_resultats_replies(self):
        texte = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(texte.count("<details>"), 6)
        self.assertEqual(texte.count("<details>"), texte.count("</details>"))
        profondeur = 0
        for ligne in texte.splitlines():
            if ligne == "<details>":
                profondeur += 1
            if "<summary>" in ligne:
                self.assertEqual(profondeur, 1)
            if "total `36`" in ligne or "total `35`" in ligne or "| 12 | 4 | 48 |" in ligne or "`16`, `28`, `40`" in ligne:
                self.assertEqual(profondeur, 1)
            if ligne == "</details>":
                profondeur -= 1
                self.assertGreaterEqual(profondeur, 0)
        self.assertEqual(profondeur, 0)
        self.assertNotIn("sans notification", texte)
        self.assertNotIn("Aucun dépôt Git", texte)


if __name__ == "__main__":
    unittest.main()
