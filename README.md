# PDS: AI Utilization — Gain Efficiency in Daily Work

Vortrags-Website der **Possehl Digital Service Factory** (Session „AI Utilization"). 16 Folien, Englisch, dunkles PDS-Design. Eine einzige HTML-Datei — kein Build, keine Abhängigkeiten.

**Live:** https://pds-ai-utilization-production.up.railway.app

## Bedienung

- **Weiter/Zurück:** Klick auf die Folie, Pfeiltasten, Leertaste, Bild auf/ab
- **Zur Startseite:** Klick auf das Logo oben links
- **Direkt zu Folie n:** URL-Anhang `#/n` (z. B. `…/#/7`), Punkte-Navigation rechts
- Feste 16:9-Bühne: sieht auf jedem Bildschirm/Beamer identisch aus

## Lokal öffnen / bearbeiten

Einfach `index.html` im Browser öffnen (Doppelklick reicht). Alle Texte, Styles und die Steuerung liegen in dieser einen Datei — Texte direkt im HTML ändern, speichern, Browser neu laden.

## ⚠️ Was noch fehlt (TODO für die Fertigstellung)

Im Deck sind **6 gestrichelte Platzhalter-Kästen** (im Code nach `class="shot"` suchen). Dort echte Screenshots/Recordings einsetzen oder live demonstrieren:

1. **Example 1 (Meeting wrap-up):** Screen-Recording — den Skill live in Possehl GPT bauen (no code)
2. **Example 2 (Dokko):** Screenshot — Dokko-Antwort mit Quellenangabe im Live-System
3. **Example 3 (Weekly report):** Animation/Recording — Agent-Lauf von Datenquellen zum Bericht
4. **Example 4 (Wissenstifter):** Ausschnitt — KI-Interview und fertiges Wissensdokument
5. **Practice A (MS 365):** Screen-Recording — Claude-Add-in in Outlook
6. **Practice B–D:** Screenshot Preferences/Vorlagen · Recording Kurzbefehl→n8n · Recording Diktat→Mail

Außerdem prüfen (Vorschlagstexte von Claude, noch nicht final abgenommen):
- **Chat-Dialoge** in den Beispiel-Fenstern (Inhalte sind plausible Beispiele, keine echten Screenshots)
- **KPI-Folie „What it's worth":** 45 min/Tag → 18,000 h/Jahr ist eine **Beispielrechnung** (als „illustrative" gekennzeichnet) — bei Bedarf durch echte Messwerte ersetzen
- **~90 %** (weniger Nacharbeit durch Korrekturliste) und **~3×** (Sprechen vs. Tippen) sind Richtwerte

Bilder einsetzen: Datei nach `assets/` legen und den `shot`-Platzhalter durch `<img src="assets/DATEI" style="width:100%;border-radius:calc(14 * var(--pxs))">` ersetzen.

## Deployment (Railway)

Gehostet auf Railway, Projekt `pds-ai-utilization` (christoph-digital's Projects), Service-ID `471c61e6-f688-4d9d-8f8f-331cf1f9093d`. Deploy nach Änderungen:

```bash
railway up --detach --service 471c61e6-f688-4d9d-8f8f-331cf1f9093d
```

(Railway-CLI nötig, eingeloggt im richtigen Workspace. Der Container ist Caddy + statische Dateien — `Dockerfile`/`Caddyfile` liegen bei.)

## Struktur

```
index.html    # alles: Folien, CSS, JS
assets/       # Factory-Logo (weiß), PD-Logo
Dockerfile    # Caddy-Container für Railway
Caddyfile
```

## Kontakt

Christoph Haß · chass@possehl.de
