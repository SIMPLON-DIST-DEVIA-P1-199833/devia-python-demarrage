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
            "Prix unitaire : 12\nQuantité : 3\nTotal : 36\n",
        )

    def test_second_jeu(self):
        self.assertEqual(
            self.executer("solution.py", (("= 12", "= 7"), ("= 3", "= 5"))),
            "Prix unitaire : 7\nQuantité : 5\nTotal : 35\n",
        )

    def test_faute_de_nom(self):
        with self.assertRaises(NameError):
            self.executer("solution.py", (("print(\"Total :\", total)", "print(totla)"),))

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
            sortie = subprocess.run([str(python), str(ROOT / "depart.py")], check=True, capture_output=True, text=True)
            self.assertEqual(sortie.stdout, "Prix unitaire : 12\nQuantité : 3\n")
            pip = subprocess.run([str(python), "-m", "pip", "--version"], check=True, capture_output=True, text=True)
            self.assertIn(str(env), pip.stdout)


if __name__ == "__main__":
    unittest.main()
