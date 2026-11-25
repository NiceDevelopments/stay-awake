"""Zentrale Produktfakten der Website – EINE Stelle für alle Sprachen (24.11.2026).

Preis/Gratisumfang und die Zahlen der Funktionsliste stehen hier. Die Sprachdateien
(tools/content_<sprache>.py) schreiben sie als Platzhalter {name}; build.py setzt sie überall ein.
Ändert sich etwas (z. B. Intervall-Grenzen, Pro-Modell): hier umstellen, `python -I tools/build.py`.

Quellen: ../CLAUDE.md, ../PRODUCT_SPEC.md, ../docs/store-eintrag.md, Code.
Die älteren Sprachdateien (en/de/es/pt/fr/id) nennen dieselben Werte noch als Klartext –
bei einer Änderung dort mit anpassen (grep nach der Zahl).
"""

FACTS = {
    "interval_min": "1",        # kürzestes Intervall: 1 Minute
    "interval_max_h": "12",     # längstes Intervall: 12 Stunden
    "interval_default": "30",   # Vorgabe: 30 Minuten
    "vibrate_s": "10",          # ohne Antwort: Vibration nach 10 s …
    "alarm_s": "20",            # … Alarm nach 20 s
    "test_alarm_s": "5",        # „Alarm testen“ läuft 5 s
    "languages": "20",          # Sprachen der App
    "reliability_points": "9",  # Punkte der Verlässlichkeitsprüfung (Screenshot „Bereit“)
}

# Preis und Gratisumfang (in jeder Sprache als Satz übersetzt, Inhalt hier festgelegt):
# - Alles, was wach hält, ist gratis (Checks, Vibration, Alarm, Zeitpläne, Verlässlichkeit).
# - Gratis zeigt ein kleines Banner auf den normalen Bildschirmen, nie im Check und nie beim Alarm.
# - „Stay Awake Pro“ entfernt das Banner: Monatsabo oder Einmalkauf; Preis nur in Google Play.
PRICE_MODEL = "free + banner; Pro = monthly subscription or one-time purchase (removes banner)"


def fill(text: str) -> str:
    for k, v in FACTS.items():
        text = text.replace("{" + k + "}", v)
    return text
