# Folder structure suggestion:
# - app.py           -> Streamlit UI
# - db.py            -> Connect to PostgreSQL and pull SIC data
# - model.py         -> Load encoder model and perform semantic matching
# - utils.py (later) -> For formatting, exporting, etc.

# Here's the initial structure of `db.py`:

import pandas as pd


def fetch_sic_data():
    df = pd.read_csv("sic_codes.csv")
    df['sic8'] = df['sic8'].astype(str).str.strip()
    df['Description'] = df['Description'].str.strip()
    return df
