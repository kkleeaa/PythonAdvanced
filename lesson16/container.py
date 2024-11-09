import streamlit as st
#with st.container():
   # st.header("This is a container")
    #st.write("This is inside the container")
#st.write("Outside the container")

st.sidebar.header("Sidebar")
st.sidebar.write("This is a sidebar")
st.sidebar.selectbox("Choose an option",["Option 1","Option 2","Option 3"])
st.sidebar.radio("Go to",["Home", "Data", "Setting"])

with st.form("my_form", clear_on_submit=True):
    name=st.text_input("Name")
    age=st.slider("Age", min_value=0, max_value=100)
    email=st.text_input("Email")
    biography=st.text_area("Short bio")
    terms=st.checkbox("I agree to the terms and conditions")
    submit_button=st.form_submit_button(label="Submit")
if submit_button:
    st.write(f"Name:{name}")
    st.write(f"Age:{age}")
    if terms:
        st.write("You have agreed to the terms and conditions")
    else:
       st.write("You have not agreed to the terms and conditions")




