import pandas as pd
import streamlit as st
#df=pd.DataFrame({
    #"Name":["Alma","Klea","Blini"],
    #"Age":[27,17,17],
   # "City":["Ferizaj","Podujeve","Podujeve"]
   # })
#st.dataframe(df)

books_df=pd.read_csv("bestsellers_with_categories_2022_03_27.csv")
st.title("Bestselling books Analysis")
st.write("This app analyzes the amazon top selling books from 2009 to 2022")

st.subheader("summary statics")
total_books=books_df.shape[0]
unique_title=books_df["Name"].nunique()
ave_rating=books_df["User Rating"].mean()
ave_price=books_df["Price"].mean()

col1,col2,col3,col4=st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique titles",unique_title)
col3.metric("Ave Rating", ave_rating)
col4.metric("Average Price", ave_price)

st.header("Dataset Preview")

with col1:
    st.subheader("Top 10 book title")
    top_titles=books_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_authors=books_df["Author"].value_counts().head(10)

st.subheader("Genre Distribution")
fig=px.pie(books_df, names="Genre",title="Most liked genre (2009-2022)", color="Genre", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart