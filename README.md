# Geo-Kreise App

Visualisieren Sie Werte pro Ort als Kreise auf einer geografisch korrekten, weiÃŸen FlÃ¤che â€“ ohne lokale Installation, ideal fÃ¼r Streamlit Cloud!

## Funktionsweise
- Laden Sie eine Excel-Datei mit den Spalten `Ort`, `Wert`, `Breitengrad`, `LÃ¤ngengrad` hoch.
- Die App zeigt die Orte als Kreise, deren GrÃ¶ÃŸe dem Wert entspricht.

## Beispiel fÃ¼r die Excel-Datei
| Ort        | Wert | Breitengrad | LÃ¤ngengrad |
|------------|------|-------------|------------|
| Nidda      | 1200 | 50.4136     | 9.0051     |
| BÃ¼dingen   | 950  | 50.2904     | 9.1127     |
| Bad Soden  | 700  | 50.1375     | 8.5042     |
| ...        | ...  | ...         | ...        |

## Nutzung auf Streamlit Cloud
1. Forken oder kopieren Sie dieses Repo auf Github.
2. Gehen Sie zu https://streamlit.io/cloud und verbinden Sie Ihr Github-Konto.
3. WÃ¤hlen Sie dieses Repo und die Datei `app.py` als App-Datei aus.
4. Laden Sie Ihre Excel-Datei hoch â€“ fertig!

## BenÃ¶tigte Dateien
- `app.py` (der Code der Anwendung)
- `geo_kreise_beispiel.xlsx` (Beispieldatei)
