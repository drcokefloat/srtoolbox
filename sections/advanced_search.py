# srtoolbox/sections/advanced_search.py
import streamlit as st
from utils.db_utils import advanced_search

def capitalize_display_name(name):
    return name.replace('_', ' ').title()

def show():
    st.title("Advanced Search")

    tool_type_options = ["", "Guidance", "Software"]
    review_family_options = ["Systematic", "Rapid", "Qualitative", "Scoping", "Mapping", "Mixed Method", "Review of Reviews", "Other"]
    review_stage_options = ["Protocol", "Search", "Screen", "Data Extract", "Quality Assess", "Synthesis", "Report", "Reference Management", "Stakeholder Engagement"]

    tool_type = st.selectbox("Tool Type", tool_type_options)
    review_family = st.multiselect("Review Family", review_family_options)
    review_stage = st.multiselect("Review Stage", review_stage_options)

    if st.button("Search"):
        # Convert display names to lowercase values for backend filtering
        filters = {
            "tool_type": tool_type.lower() if tool_type else "",
            "review_family": [rf.lower().replace(" ", "_") for rf in review_family],
            "review_stage": [rs.lower().replace(" ", "_") for rs in review_stage]
        }
        results = advanced_search(filters)
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