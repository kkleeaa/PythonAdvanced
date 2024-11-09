import streamlit as st




def main():
    st.title("Hello, from Streamlit")
    if st.button("Click girl"):
        st.write("Go survive the day girl")
    st.checkbox("Check me")
    st.write("You're seeing this cuz u survived the day")


    user_input_text=st.text_input("Eneter text","Sample")
    st.write("You entered", user_input_text)
    user_input_number=st.number_input("Enter your age", min_value=0, max_value=100)
    st.write("You input", user_input_number)
    user_input_textarea=st.text_area("Enter ur message")
    st.write(f"Message:{user_input_textarea}")
    user_input_radio=st.radio("Pick one",["Option1","Option2","Option3"])
    st.write(f"You choose:{user_input_radio}")
    if st.button("Success"):
        st.success("Operation was successful")
        






if __name__=="__main__":
    main()
