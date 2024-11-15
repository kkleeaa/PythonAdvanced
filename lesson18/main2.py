import pandas as pd
import streamlit as st
import plotly.express as px



#df=pd.DataFrame({
    #"Name":["Alma","Klea","Blini"],
    #"Age":[27,17,17],
   # "City":["Ferizaj","Podujeve","Podujeve"]
   # })
#st.dataframe(df)

filtered_df=pd.read_csv("bestsellers_with_categories_2022_03_27.csv")
st.title("Bestselling books Analysis")
st.write("This app analyzes the amazon top selling books from 2009 to 2022")

st.subheader("summary statics")
total_books=filtered_df.shape[0]
unique_title=filtered_df["Name"].nunique()
ave_rating=filtered_df["User Rating"].mean()
ave_price=filtered_df["Price"].mean()

col1,col2,col3,col4=st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique titles",unique_title)
col3.metric("Ave Rating", ave_rating)
col4.metric("Average Price", ave_price)

st.header("Dataset Preview")

with col1:
    st.subheader("Top 10 book title")
    top_titles=filtered_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_authors=filtered_df["Author"].value_counts().head(10)

st.subheader("Genre Distribution")
fig=px.pie(filtered_df, names="Genre",title="Most liked genre (2009-2022)", color="Genre", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of fiction vs non-fiction books over the years")
size=filtered_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig=px.bar(size,x='Year',y='Genre', color='Genre', title='Number of fiction vs non-fiction books from 2009-2022', color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')
st.plotly_chart(fig)


st.subheader("Top 15 authors by counts of books published(2009-2022)")
top_authors=filtered_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']
fig=px.bar(top_authors, x='Count', y='Author', orientation='h',
           title='Top 15 author by counts of books published',
           labels={'Count': 'Counts of books published', 'Author':'Author'},
           color='Count', color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter data by genre")
genre_filter= st.selectbox("Select Genre", filtered_df['Genre'].unique())
filtered_df= filtered_df[filtered_df['Genre']==genre_filter]
st.write(filtered_df)

st.sidebar.header("Add new book data")
with st.sidebar.form("book_form"):
    new_name=st.text_input("Book Name")
    new_author=st.text_input("Author")
    new_user_rating=st.slider("User Rating", 0.0,5.0,0.0,0.1)
    new_reviews=st.number_input("Review", min_value=0, step=1)
    new_price=st.number_input("Price", min_value=0, step=1)
    new_year=st.number_input("Year", min_value=2009, max_value=2022, step=1)
    mew_genre=st.selectbox("Genre", filtered_df["Genre"].unique())
    submit_button=st.form_submit_button(label="Add new book")
if submit_button:
    new_data={
        "Name":new_name,
        "Author": new_author,
        "User Rating": new_user_rating,
        "Reviews": new_reviews,
        "Price": new_price,
        "Year": new_year,
        "Genre": new_genre
    }
    books_df=pd.concat([pd.DataFrame(new_data, index=[0]), filtered_df],ignore_index=True)
    books_df.to_csv("bestsellers_with_categories_2022_03_27.csv", index=False)
    st.sidebar.success("New book added")


st.sidebar.header("Filter Options: ")
selected_author=st.sidebar.selectbox("Select author",["All"]+list(filtered_df["Author"].unique()))
selected_year=st.sidebar.selectbox("Select year",["All"]+list(filtered_df["Year"].unique()))
selected_genre=st.sidebar.selectbox("Select genre", ["All"]+list(filtered_df["Genre"].unique()))
min_rating= st.sidebar.slider("Minimum user rating",0.0,5.0,0.0,0.1)
max_price=st.sidebar.slider("Maximum price",0,filtered_df["Price"].max(), filtered_df["Price"].max())

filtered_df=filtered_df.copy()
if selected_author!="All":
    filtered_df=filtered_df[filtered_df["Author"]==selected_author]
if selected_year!="All":
    filtered_df=filtered_df[filtered_df["Year"]==selected_year]
if selected_genre!="All":
    filtered_df=filtered_df[filtered_df["Genre"]==selected_genre]
filtered_df=filtered_df[
    (filtered_df["User Rating"]>min_rating)&(filtered_df["Price"]<=max_price)
]













