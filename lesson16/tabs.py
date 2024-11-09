import streamlit as st
tab1,tab2,tab3=st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.header("Tab 1")
    st.write("content")

with tab2:
    st.header("Tab 2")
    st.write("content")
with tab3:
    st.header("Tab 3")
    st.write("content")