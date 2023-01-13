import streamlit as st
import rec_algorithms
import fetching_function
import pandas as pd
# rec_algorithms.user_base_recommender_using_KNNBaseline(610, 5)[0]
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
links = pd.read_csv('links.csv')
# get categories from the movies dataframe
categories = movies['genres'].str.get_dummies(sep='|').columns[1::]
# increase the font size and the width of the title
st.title("Welcome to WBSFLIX")
col1, col2, col3, col4 = st.columns(4)
# give maximun width to the searchbar
col2, col3 = st.columns((2, 1))
search = col2.text_input("Search for a movie")
buttonSearch = col2.button("Search")
# enter id
login = col3.text_input("log in with the ID number")
buttonLogin = col3.button("log in to WBSFLIX")
# loop through the list of movies
dropdown = st.selectbox("Select a genre", categories)
# give equal size to the 4 columns
mcol1, mcol2, mcol3, mcol4, mcol5 = st.columns((1, 1, 1, 1, 1))

# display the title of the section first
st.write("""
# All time classics""")

mcol1.image(fetching_function.get_movie_img(
    rec_algorithms.recommend("", 5)[0]), width=150,  caption=rec_algorithms.recommend("", 5)[0])
mcol2.image(fetching_function.get_movie_img(rec_algorithms.recommend(
    "", 5)[1]), width=150, caption=rec_algorithms.recommend("", 5)[1])
mcol3.image(fetching_function.get_movie_img(rec_algorithms.recommend(
    "", 5)[2]), width=150, caption=rec_algorithms.recommend("", 5)[2])
mcol4.image(fetching_function.get_movie_img(rec_algorithms.recommend(
    "", 5)[3]), width=150, caption=rec_algorithms.recommend("", 5)[3])
mcol5.image(fetching_function.get_movie_img(rec_algorithms.recommend(
    "", 5)[4]), width=150, caption=rec_algorithms.recommend("", 5)[4])
mcol1, mcol2, mcol3, mcol4, mcol5 = st.columns((1, 1, 1, 1, 1))
st.write("""
# Our """+dropdown+""" favorites""")
if dropdown:

    mcol1.image(fetching_function.get_movie_img(
        rec_algorithms.recommend_genre(dropdown, 5)[0]), width=150,  caption=rec_algorithms.recommend_genre(dropdown, 5)[0])
    mcol2.image(fetching_function.get_movie_img(rec_algorithms.recommend_genre(
        dropdown, 5)[1]), width=150, caption=rec_algorithms.recommend_genre(dropdown, 5)[1])
    mcol3.image(fetching_function.get_movie_img(rec_algorithms.recommend_genre(
        dropdown, 5)[2]), width=150, caption=rec_algorithms.recommend_genre(dropdown, 5)[2])
    mcol4.image(fetching_function.get_movie_img(rec_algorithms.recommend_genre(
        dropdown, 5)[3]), width=150, caption=rec_algorithms.recommend_genre(dropdown, 5)[3])
    mcol5.image(fetching_function.get_movie_img(rec_algorithms.recommend_genre(
        dropdown, 5)[4]), width=150, caption=rec_algorithms.recommend_genre(dropdown, 5)[4])
mcol1, mcol2, mcol3, mcol4, mcol5 = st.columns((1, 1, 1, 1, 1))
st.write("""
    # Because you searched for """ + search + """
    """)
if buttonSearch:

    mcol1.image(fetching_function.get_movie_img(
        rec_algorithms.recommend(search, 5)[0]), width=150,  caption=rec_algorithms.recommend(search, 5)[0])
    mcol2.image(fetching_function.get_movie_img(rec_algorithms.recommend(
        search, 5)[1]), width=150, caption=rec_algorithms.recommend(search, 5)[1])
    mcol3.image(fetching_function.get_movie_img(rec_algorithms.recommend(
        search, 5)[2]), width=150, caption=rec_algorithms.recommend(search, 5)[2])
    mcol4.image(fetching_function.get_movie_img(rec_algorithms.recommend(
        search, 5)[3]), width=150, caption=rec_algorithms.recommend(search, 5)[3])
    mcol5.image(fetching_function.get_movie_img(rec_algorithms.recommend(
        search, 5)[4]), width=150, caption=rec_algorithms.recommend(search, 5)[4])
mcol1, mcol2, mcol3, mcol4, mcol5 = st.columns((1, 1, 1, 1, 1))
st.write("""### FOR YOU, User""" + login +
         """ cosine suggests these movies:""")
st.write("""# FOR YOU, User""" + login + """ svd suggests these movies:
""")
if buttonLogin:

    mcol1.image(fetching_function.get_movie_img(
        rec_algorithms.user_based_recommender(search, 5)[0]), width=150,  caption=rec_algorithms.user_based_recommender(login, 5)[0])
    mcol2.image(fetching_function.get_movie_img(rec_algorithms.user_based_recommender(
        search, 5)[1]), width=150, caption=rec_algorithms.user_based_recommender(login, 5)[1])
    mcol3.image(fetching_function.get_movie_img(rec_algorithms.user_based_recommender(
        login, 5)[2]), width=150, caption=rec_algorithms.user_based_recommender(login, 5)[2])
    mcol4.image(fetching_function.get_movie_img(rec_algorithms.user_based_recommender(
        login, 5)[3]), width=150, caption=rec_algorithms.user_based_recommender(login, 5)[3])
    mcol5.image(fetching_function.get_movie_img(rec_algorithms.user_based_recommender(
        login, 5)[4]), width=150, caption=rec_algorithms.user_based_recommender(login, 5)[4])

    mcol1.image(fetching_function.get_movie_img(
        rec_algorithms.user_base_recommender_using_svd(search, 5)[0]), width=150,  caption=rec_algorithms.recommend(login, 5)[0])
    mcol2.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_svd(
        search, 5)[1]), width=150, caption=rec_algorithms.user_base_recommender_using_svd(login, 5)[1])
    mcol3.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_svd(
        login, 5)[2]), width=150, caption=rec_algorithms.user_base_recommender_using_svd(login, 5)[2])
    mcol4.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_svd(
        login, 5)[3]), width=150, caption=rec_algorithms.user_base_recommender_using_svd(login, 5)[3])
    mcol5.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_svd(
        login, 5)[4]), width=150, caption=rec_algorithms.user_base_recommender_using_svd(login, 5)[4])
    # mcol1, mcol2, mcol3, mcol4, mcol5 = st.columns((1, 1, 1, 1, 1))
    # st.write("""
    #     # FOR YOU, User""" + login + """ KNNBaseline suggests these movies:
    #     """)
    # mcol1.image(fetching_function.get_movie_img(
    #     rec_algorithms.user_base_recommender_using_KNNBaseline(search, 5)[0]), width=150,  caption=rec_algorithms.recommend(login, 5)[0])
    # mcol2.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_KNNBaseline(
    #     search, 5)[1]), width=150, caption=rec_algorithms.user_base_recommender_using_KNNBaseline(login, 5)[1])
    # mcol3.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_KNNBaseline(
    #     login, 5)[2]), width=150, caption=rec_algorithms.user_base_recommender_using_KNNBaseline(login, 5)[2])
    # mcol4.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_KNNBaseline(
    #     login, 5)[3]), width=150, caption=rec_algorithms.user_base_recommender_using_KNNBaseline(login, 5)[3])
    # mcol5.image(fetching_function.get_movie_img(rec_algorithms.user_base_recommender_using_KNNBaseline(
    #     login, 5)[4]), width=150, caption=rec_algorithms.user_base_recommender_using_KNNBaseline(login, 5)[4])
    # mcol1, mcol2, mcol3, mcol4, mcol5 = st.columns((1, 1, 1, 1, 1))
