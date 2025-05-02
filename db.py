# Folder structure suggestion:
# - app.py           -> Streamlit UI
# - db.py            -> Connect to PostgreSQL and pull SIC data
# - model.py         -> Load encoder model and perform semantic matching
# - utils.py (later) -> For formatting, exporting, etc.

# Here's the initial structure of `db.py`:

import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def fetch_sic_data():
    query = '''
        SELECT sic8, "Description", "Notes", "L1", "L2", "L3", "L4"
        FROM public."SIC_Code_Repository"
        WHERE "Description" IS NOT NULL
    '''
    conn = get_connection()
    df = pd.read_csv("sic_codes.csv")
    conn.close()
    df['sic8'] = df['sic8'].astype(str).str.strip()
    df['Description'] = df['Description'].str.strip()
    return df
