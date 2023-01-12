import streamlit as st
import rec_algorithms
import pandas as pd
# rec_algorithms.user_base_recommender_using_KNNBaseline(610, 5)[0]
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
links = pd.read_csv('links.csv')
# get categories from the movies dataframe
categories = movies['genres'].str.get_dummies(sep='|').columns[1::]
st.title("WELCOME TO WBSFLIX")
# create a searchbar
search = st.text_input("Search for a movie")
buttonSearch = st.button("Search")
# enter id
login = st.text_input("log in with the ID number")
buttonLogin = st.button("log in to WBSFLIX")
# loop through the list of movies
dropdown = st.selectbox("Select a genre", categories)
st.write("""
### All time classics""")
for i in rec_algorithms.recommend("", 10):
    st.write(i)
if dropdown:
    st.write("""
### Our """+dropdown+""" favorites""")
    for i in rec_algorithms.recommend_genre("Crime", 5):
        st.write(i)
if buttonSearch:
    st.write("""
    ### Because you searched for """ + search + """
    """)
    for i in rec_algorithms.item_based_recommender(search, 5):
        st.write(i)
if buttonLogin:
    st.write("""### FOR YOU, User""" + login +
             """ cosine suggests these movies:""")
    for i in rec_algorithms.user_based_recommender(int(login), 5):
        if rec_algorithms.user_based_recommender(int(login), 5) == "User not found":
            st.write("User not found")
            break
        else:
            st.write(i)
    st.write("""
### FOR YOU, User""" + login + """ KNNBaseline suggests these movies:
""")
    for i in rec_algorithms.user_base_recommender_using_KNNBaseline(login, 5):
        st.write(i)
    st.write("""### FOR YOU, User""" + login +
             """ SVD suggests these movies:""")
    for i in rec_algorithms.user_base_recommender_using_svd(int(login), 5):
        st.write(i)
