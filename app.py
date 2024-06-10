import streamlit as st

st.set_page_config(
    page_title="The Systematic Review Toolbox",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add logo and title to the sidebar
st.sidebar.image("logo.png", width = 150)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Quick Search", "Advanced Search", "About"])

if page == "Quick Search":
    from sections import quick_search
    quick_search.show()
elif page == "Advanced Search":
    from sections import advanced_search
    advanced_search.show()
elif page == "About":
    from sections import about
    about.show()