"""Personnalite Heimdall : preset disponible et reconnu a la voix."""
import unittest

from core import personnalite


class HeimdallTest(unittest.TestCase):
    def test_preset_se_presente_comme_heimdall(self):
        self.assertIn("Heimdall", personnalite.persona("heimdall"))

    def test_formulations_vocales(self):
        for dit in ("heimdall", "passe en mode Heimdall", "mode gardien"):
            self.assertEqual(personnalite.normaliser(dit), "heimdall")

    def test_presets_existants_inchanges(self):
        self.assertEqual(personnalite.normaliser("mode jarvis"), "jarvis_sarcastique")
        self.assertEqual(personnalite.normaliser("neutre"), "neutre")


if __name__ == "__main__":
    unittest.main()
