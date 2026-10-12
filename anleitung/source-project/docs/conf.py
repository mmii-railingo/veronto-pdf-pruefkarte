# SPDX-License-Identifier: MIT
"""Build configuration for the independent PDF-Prüfkarte documentation."""

import os

project = "PDF-Prüfkarte: Bedienung und Technik"
author = "Martin Meng, veronto GmbH & Co. KG"
copyright = "2026, veronto GmbH & Co. KG"
release = "1.0"
language = "de"
extensions = []
root_doc = "index"
exclude_patterns = []
html_theme = "alabaster"
html_title = project
html_show_sourcelink = True
html_show_sphinx = False
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
html_theme_options = {
    "description": "Freie Dokumentation für eine interaktive Arbeitshilfe",
    "fixed_sidebar": True,
}
