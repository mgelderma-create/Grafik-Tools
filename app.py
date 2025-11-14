
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Geo-Kreise nach Wert", layout="wide")

st.title("Orte als Kreise – geografisch positioniert")
st.write("""
**Laden Sie eine Excel-Datei mit Spalten für Ort, Wert, Breitengrad und Längengrad hoch.**
Die Größe der Kreise entspricht dem Wert. Die Orte werden geografisch korrekt auf einer weißen Fläche angezeigt.
""")

uploaded_file = st.file_uploader("Excel-Datei hochladen", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    # Spaltennamen prüfen
    required_cols = {"Ort", "Wert", "Breitengrad", "Längengrad"}
    if not required_cols.issubset(df.columns):
        st.error(f"Die Datei muss die Spalten {required_cols} enthalten.")
    else:
        # Achsen skalieren
        df["Längengrad_skal"] = df["Längengrad"] * 0.65
        df["Breitengrad_skal"] = df["Breitengrad"] * 1.24
        
        # Plotly-Scatterplot auf weißem Hintergrund
        fig = px.scatter(
            df,
            x="Längengrad_skal",
            y="Breitengrad_skal",
            size="Wert",
            text="Ort",
            size_max=80,
            color_discrete_sequence=["#0066b3"],
            labels={"Längengrad_skal": "Longitude", "Breitengrad_skal": "Latitude"},
        )
        fig.update_traces(
            marker=dict(line=dict(width=2, color="white")),
            textposition='middle center',
            textfont=dict(color="white")
        )
        fig.update_layout(
    yaxis=dict(
        showgrid=False,
        zeroline=False
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    xaxis=dict(showgrid=False, zeroline=False),
    margin=dict(l=20, r=20, t=40, b=20),
    height=800,
        )

        st.plotly_chart(fig, use_container_width=True)
        st.success("Karte erfolgreich erstellt! Sie können die Grafik per Rechtsklick speichern.")

else:
    st.info("Bitte laden Sie eine Excel-Datei hoch.")

st.markdown("---")
st.markdown("**Hinweis:** Die Kreise sind auf einer weißen Fläche positioniert, nicht auf einer Straßenkarte.")
