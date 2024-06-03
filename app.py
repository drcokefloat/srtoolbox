import streamlit as st
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def create_connection():
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client['srtoolbox']
    return client, db

def close_connection(client):
    client.close()

def main():
    st.title("The Systematic Review Toolbox")

    st.subheader("Quick Search")
    with st.form(key='quick_search_form'):
        quick_search = st.text_input("Try searching for a tool...")
        submit_button = st.form_submit_button(label='Search')

    if submit_button:
        if quick_search:
            search_tools(quick_search)

def search_tools(search_term):
    client, db = create_connection()
    collection = db['tools']
    
    query = {"tool_name": {"$regex": search_term, "$options": "i"}}
    projection = {"_id": 0, "tool_name": 1, "tool_summary": 1, "tool_link": 1}
    
    results = collection.find(query, projection)
    results_df = pd.DataFrame(list(results))
    
    if not results_df.empty:
        for _, row in results_df.iterrows():
            st.write(f"**Name:** {row['tool_name']}")
            st.write(f"**Summary:** {row['tool_summary']}")
            st.write(f"**URL:** [Link]({row['tool_link']})")
            st.write("---")
    else:
        st.write("No results found.")
    
    close_connection(client)

if __name__ == "__main__":
    main()