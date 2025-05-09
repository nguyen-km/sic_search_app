import pandas as pd


def fetch_sic_data():
    df = pd.read_excel("sic_codes.xlsx")
    df['sic8'] = df['sic8'].astype(str).str.strip()
    df['Description'] = df['Description'].str.strip()
    df['type'] = df['type'].str.strip()
    return df
