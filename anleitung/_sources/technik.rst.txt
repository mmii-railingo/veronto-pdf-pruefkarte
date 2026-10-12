Technischer Aufbau
=======================

Die Prüfkarte besteht aus einer statischen HTML-Datei. Darin stehen die
Struktur, die CSS-Regeln und ein kleines JavaScript. Der öffentlich
einsehbare Stand liegt im `Repository der Prüfkarte
<https://github.com/mmii-railingo/veronto-pdf-pruefkarte>`_. Dieses
Dokumentationsprojekt enthält eigene Texte und Builddateien; der Code
der Prüfkarte wird hier nicht mitgeliefert.

Bedienelemente
-------------------

Die neun Schritte verwenden native Checkboxen. Jede Checkbox steht in einem
``label`` zusammen mit ihrer Beschriftung. Die drei Gruppen besitzen
Überschriften, die über ``aria-labelledby`` zugeordnet sind. Der
Fortschritt verwendet ``role="status"`` und ``aria-live="polite"``.
Diese Eigenschaften unterstützen die Bedienung mit Tastatur und
Sprachausgabe. Prüfe konkrete Browser und Hilfsmittel bei einer Änderung
weiterhin selbst.

Zustand und Ereignisse
---------------------------

Beim Laden sammelt das Skript die Checkboxen in einer Liste. Auf jedes
``change``-Ereignis zählt es die aktuell gesetzten Häkchen und aktualisiert
den sichtbaren Fortschritt. Der Druckknopf ruft ``window.print()`` auf.
Das Skript verwendet weder ``localStorage`` noch ``sessionStorage`` und
sendet keine Prüfergebnisse an einen eigenen Endpunkt.

Ein Browser kann Formularzustände bei einer Navigation wiederherstellen.
Die Karte synchronisiert den Zähler im betrachteten Stand ausschließlich
bei einer Änderung eines Kästchens. Wenn Browser und Fortschrittsanzeige
nach einer Wiederherstellung abweichen, prüfe die Häkchen erneut und löse
eine Änderung aus. Verlasse dich bei längeren Vorgängen auf deinen gesicherten
Prüfvermerk.

Darstellung und Druck
--------------------------

Die Seite nutzt Systemschriften und CSS für schmale Bildschirme. Unter
540 Pixeln Breite verändert sich unter anderem die Anordnung des
Fortschrittsbereichs. Die Druckregeln entfernen den Druckknopf, setzen
einen weißen Hintergrund und versuchen, die einzelnen Gruppen auf einer
Seite zusammenzuhalten. Die tatsächliche Seitenaufteilung hängt vom
Druckdialog, Papierformat und Browser ab.

Dateiverarbeitung
----------------------

Die Prüfkarte besitzt keinen Datei-Upload und keinen PDF-Parser. Sie liest
keine Dokumente ein und untersucht keine Textschichten oder Metadaten.
Du öffnest deine PDF-Datei in einem geeigneten Programm. Der Aufruf einer
gehosteten Seite bleibt ein gewöhnlicher Abruf bei ihrem Hostinganbieter;
die Aussage über das Skript beschreibt keine allgemeine Eigenschaft des
Browsers, des Druckdienstes oder verlinkter Werkzeuge.

Die Dokumentation bauen
----------------------------

Diese Dokumentation verwendet Sphinx und reStructuredText. Für einen
lokalen Build brauchst du Python ab Version 3.11. Im vorgesehenen
Read-the-Docs-Build wird Python 3.12 eingesetzt.

Führe im Stammordner dieses Dokumentationsprojekts aus:

.. code-block:: console

   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   .venv/bin/python -m sphinx -b html -W --keep-going docs _build/html

Öffne danach ``_build/html/index.html``. Der Build schlägt bei Warnungen
fehl, damit beispielsweise ungültige interne Verweise auffallen. Externe
Zielseiten müssen zusätzlich geprüft werden. Die Datei
``.readthedocs.yaml`` legt Buildsystem, Pythonversion und Anforderungen
für einen öffentlichen Read-the-Docs-Build fest. Eine Veröffentlichung
benötigt zusätzlich ein dort angelegtes Projekt.
