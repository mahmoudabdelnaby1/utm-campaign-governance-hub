import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from url_cleaner import sanitize_utm_url

class TestCleaner(unittest.TestCase):
    def test_sanitize(self):
        raw = "https://store.sa/?utm_source=Meta%20Ads&utm_medium=CPC&utm_campaign=Saudi%20Offer"
        clean = sanitize_utm_url(raw)
        self.assertIn("utm_source=meta_ads", clean)
        self.assertIn("utm_medium=cpc", clean)

if __name__ == "__main__":
    unittest.main()
