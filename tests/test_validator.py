"""
Unit tests for UTM Validator
"""
import unittest
from src.utm_validator import validate_utm

class TestUTMValidator(unittest.TestCase):
    def test_valid_utm(self):
        url = "https://brand.com/?utm_source=google&utm_medium=cpc&utm_campaign=summer_2026"
        res = validate_utm(url)
        self.assertTrue(res["valid"])
        self.assertEqual(len(res["errors"]), 0)

    def test_missing_campaign_and_spaces(self):
        url = "https://brand.com/?utm_source=facebook&utm_medium=paid social"
        res = validate_utm(url)
        self.assertFalse(res["valid"])
        self.assertTrue(any("Missing required parameter 'utm_campaign'" in e for e in res["errors"]))
        self.assertTrue(any("contains spaces" in e for e in res["errors"]))

    def test_canonical_cleaning(self):
        url = "https://brand.com/?utm_source=Snapchat&utm_medium=PAID-SOCIAL&utm_campaign=Flash%20Sale"
        res = validate_utm(url)
        self.assertEqual(res["canonical_url"], "https://brand.com/?utm_source=snapchat&utm_medium=paid-social&utm_campaign=flash-sale")

if __name__ == "__main__":
    unittest.main()
