# PDF-Prüfkarte: Bedienung und Technik

Eigenständige freie Dokumentation der interaktiven Arbeitshilfe unter
https://mmii-railingo.github.io/veronto-pdf-pruefkarte/.

Das Projekt enthält eine Bedienungsanleitung, eine Beschreibung der beobachteten
Technik und Hinweise für die Dokumentationspflege. Die ursprüngliche Prüfkarte
wird hier weder kopiert noch neu lizenziert.

## Lokal bauen

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m sphinx -b html -W --keep-going docs _build/html
```

Öffne anschließend `_build/html/index.html`. Read the Docs verwendet die
Konfiguration `.readthedocs.yaml` und baut mit Python 3.12.

## Lizenz

Neu verfasste Texte: CC BY 4.0, siehe `LICENSE-DOCS.md`.
Neue Build- und Konfigurationsdateien: MIT, siehe `LICENSE-CONFIG.txt`.
Externe Pakete und die ursprüngliche Prüfkarte behalten ihre jeweiligen Rechte.
