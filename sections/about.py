import streamlit as st

def show():
    st.title("About")

    st.markdown("""
    <p>The Systematic Review Toolbox is an online catalogue of tools that support various tasks within the systematic review and wider evidence synthesis process. It was developed and founded by <a href="https://twitter.com/drcokefloat">Dr Christopher Marshall</a> and <a href="https://www.sheffield.ac.uk/scharr/people/staff/anthea-sutton">Anthea Sutton</a>, launching in 2014.</p>
    <p>In 2022, the Systematic Review Toolbox underwent a significant update. This included:</p>
    <ul>
    <li>New categorisation of guidance and software tools in accordance with the systematic review taxonomy presented in <a href="https://onlinelibrary.wiley.com/doi/abs/10.1111/hir.12276">Sutton <i>et al.</i> 2019</a>.</li>
    <li>Updating the records to reflect what stage of the review process tools aim to address.</li>
    <li>Checking each record to assess when the tool was last updated, or when the most recent related publication was published.</li>
    <li>Checking individual records and links to ensure all tools are currently active and available.</li>
    <li>Developing a modern website with improved accessibility.</li>
    </ul>
    <p>The latest tools added to the Systematic Review Toolbox are posted to our Twitter account: <a href="https://twitter.com/srtoolbox">@srtoolbox</a></p>
    <p><b>How to cite:</b> Marshall, C., Sutton, A., O'Keefe, H., Johnson, E. (Eds.). (2022). The Systematic Review Toolbox. Available from: <a href="http://www.systematicreviewtools.com/">http://www.systematicreviewtools.com/</a></p>
    """, unsafe_allow_html=True)