import streamlit as st
import pandas as pd
from db import fetch_sic_data
from model import SICSemanticMatcher

# Load data from DB and initialize matcher
st.title("🔍 SIC Code Finder")
st.write("Paste a contract description or firm summary to get relevant SIC codes.")

@st.cache_resource

def load_model_and_data():
    df = fetch_sic_data()
    matcher = SICSemanticMatcher(df['Description'].tolist())
    return df, matcher


df, matcher = load_model_and_data()

# User input
query = st.text_area("Enter description:", height=150)

if query:
    top_indices, scores = matcher.match(query, top_k=20)
    results = df.iloc[top_indices].copy()
    results['Similarity'] = (1 - scores).round(3)

    # Display results
    st.subheader("Top 20 Matches:")
    # st.dataframe(results[['sic8', 'Description', 'Similarity', 'L1', 'L2', 'L3', 'L4']])

    rows = []
    for _, row in results[['sic8', 'Description', 'type']].iterrows():
        rows.append(f"<tr><td style='white-space:nowrap;padding:4px 10px;'>{row['sic8']}</td>"
                    f"<td style='padding:4px 10px;'>{row['Description']}</td>"
                    f"<td style='padding:4px 10px;'>{row['type']}</td></tr>"
                    )

    table_html = f"""
    <table style='border-collapse:collapse; width:100%; font-family:monospace;'>
    <thead>
        <tr>
        <th style='text-align:left; padding:4px 10px;'>SIC Code</th>
        <th style='text-align:left; padding:4px 10px;'>Description</th>
        <th style='text-align:left; padding:4px 10px;'>Type</th>
        </tr>
    </thead>
    <tbody>
        {''.join(rows)}
    </tbody>
    </table>
    """

    st.markdown(table_html, unsafe_allow_html=True)

else:
    st.info("Enter a description above to see suggestions.")
