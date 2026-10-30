#!/usr/bin/env python3
import re
import sys
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def sanitize_utm_url(raw_url):
    u = urlparse(raw_url)
    q = parse_qs(u.query)
    clean_q = {}
    for k, vals in q.items():
        clean_k = k.strip().lower()
        clean_v = [re.sub(r'\s+', '_', v.strip().lower()) for v in vals]
        clean_q[clean_k] = clean_v

    new_query = urlencode(clean_q, doseq=True)
    return urlunparse((u.scheme, u.netloc, u.path, u.params, new_query, u.fragment))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sanitize_utm_url(sys.argv[1]))
