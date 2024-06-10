import streamlit as st
from utils.db_utils import search_tools

def capitalize_display_name(name):
    return name.replace('_', ' ').title()

def show():
    st.title("Quick Search")

    with st.form(key='quick_search_form'):
        quick_search = st.text_input("Try searching for a tool...")
        submit_button = st.form_submit_button(label='Search')

    if submit_button:
        results = search_tools(quick_search)
        result_count = len(results)
        st.write(f"Number of results: {result_count}")
        if results:
            for tool in results:
                st.markdown(f"### Name: {tool['tool_name']}")
                st.markdown(f"**Summary:** {tool['tool_summary']}")
                st.markdown(f"**URL:** [Link]({tool['url_to_tool']})")
                review_families = ', '.join([capitalize_display_name(k) for k, v in tool['review_families'].items() if v])
                st.markdown(f"**Review Families:** {review_families}")
                review_stages = ', '.join([capitalize_display_name(k) for k, v in tool['review_stages'].items() if v])
                st.markdown(f"**Review Stages:** {review_stages}")
        else:
            st.write("No tools found.")