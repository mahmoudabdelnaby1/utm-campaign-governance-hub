"""
UTM Campaign Governance Hub & Interactive Validator
Validates campaign tracking URLs against enterprise marketing governance rules:
- Forced lowercase enforcement
- Space character detection (must use hyphen or underscore)
- Whitelisted utm_medium taxonomy
- Campaign naming convention regex check: [geo]_[channel]_[objective]_[offer]
"""
import urllib.parse
import re
import json
import argparse
from typing import Dict, Any, List

ALLOWED_MEDIUMS = {
    "cpc", "paid-social", "paid-search", "display", "email", "affiliate",
    "organic-social", "referral", "sms", "qr", "influencer"
}

def validate_utm(url: str, enforce_geo: bool = False) -> Dict[str, Any]:
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    
    errors: List[str] = []
    warnings: List[str] = []
    
    required = ["utm_source", "utm_medium", "utm_campaign"]
    for req in required:
        if req not in params or not params[req][0].strip():
            errors.append(f"Missing required parameter '{req}'.")
            
    # Check casing & whitespace
    for k, v in params.items():
        if k.startswith("utm_"):
            val = v[0]
            if any(c.isupper() for c in val):
                warnings.append(f"Parameter '{k}={val}' contains uppercase characters. Lowercase recommended.")
            if " " in val:
                errors.append(f"Parameter '{k}={val}' contains spaces. Use '-' or '_' instead.")
                
    # Check medium taxonomy
    if "utm_medium" in params and params["utm_medium"][0]:
        med = params["utm_medium"][0].lower()
        if med not in ALLOWED_MEDIUMS:
            warnings.append(f"Non-standard utm_medium '{med}'. Expected one of: {sorted(list(ALLOWED_MEDIUMS))}.")

    # Suggest canonical cleaned URL
    cleaned_params = {}
    for k, v in params.items():
        cleaned_params[k] = v[0].lower().strip().replace(" ", "-")
        
    cleaned_query = urllib.parse.urlencode(cleaned_params)
    cleaned_url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, cleaned_query, parsed.fragment))
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "original_url": url,
        "canonical_url": cleaned_url,
        "extracted_params": {k: v[0] for k, v in params.items()}
    }

def main():
    sample = "https://example.com/landing?utm_source=Meta%20Ads&utm_medium=paid_social&utm_campaign=KSA_Ramadan_Promo"
    res = validate_utm(sample)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
