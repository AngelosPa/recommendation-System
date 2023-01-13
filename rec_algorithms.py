# recommender function
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from surprise import SVD, KNNBaseline, KNNBasic, KNNWithMeans, KNNWithZScore,  NormalPredictor, BaselineOnly, CoClustering
from surprise import Dataset
from surprise import Reader
pd.options.mode.chained_assignment = None  # default='warn'
movies_original = pd.read_csv('movies.csv')
ratings_original = pd.read_csv('ratings.csv')
links_original = pd.read_csv('links.csv')
reader = Reader()
reader = Reader(rating_scale=(0.5, 5))
svd = SVD()
KNNBaseline = KNNBaseline()
KNNBasic = KNNBasic()
KNNWithMeans = KNNWithMeans()
KNNWithZScore = KNNWithZScore()
movies = movies_original.copy()
ratings = ratings_original.copy()


def user_base_recommender_using_svd(user_id, n):
    # find best movie according to svd
    movies = movies_original.copy()
    ratings = ratings_original.copy()
    # get the ratings that the user has not rated
    ratings_not_rated_by_user = ratings.loc[ratings['userId'] != user_id]

    data = Dataset.load_from_df(
        ratings_not_rated_by_user[['userId', 'movieId', 'rating']], reader)
    # cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    trainset = data.build_full_trainset()
    svd.fit(trainset)
    # sort the movies upon the highest accuracy of prediction
    ratings_not_rated_by_user['est'] = ratings_not_rated_by_user.apply(
        lambda x: svd.predict(x['userId'], x['movieId']).est, axis=1)
    ratings_not_rated_by_user = ratings_not_rated_by_user.sort_values(
        by='est', ascending=False)
    # get the top n movies
    return movies_original.loc[movies_original['movieId'].isin(ratings_not_rated_by_user.head(n)['movieId'])]['title'].tolist()


def user_based_recommender(user_id, n):
    movies = movies_original.copy()
    ratings = ratings_original.copy()

    if len(ratings.loc[ratings['userId'] == user_id]):
        # user based approach using cosine similarity

        # user item matrix
        users_crosstab_original = ratings.pivot_table(
            index='userId', columns='movieId', values='rating')
        users_crosstab_original.fillna(0, inplace=True)
        users_crosstab = users_crosstab_original.copy()
        # user similarity matrix
        user_similarity = cosine_similarity(users_crosstab)
        # turn similarities to weights
        user_similarity = MinMaxScaler().fit_transform(user_similarity)
        # estimate the missing ratings
        user_predicted_ratings = np.dot(user_similarity, users_crosstab)
        # turn the predicted ratings to a dataframe
        user_predicted_ratings = pd.DataFrame(
            user_predicted_ratings, index=users_crosstab.index, columns=users_crosstab.columns)
        # get the movies that the user has already rated
        user_rated = users_crosstab.loc[user_id, :]
        # get the movies that the user has not rated
        user_not_rated = user_rated[user_rated == 0]
        # get the movies that the user has not rated and sort them by the predicted ratings
        user_predicted_ratings = user_predicted_ratings.loc[user_id,
                                                            user_not_rated.index]
        user_predicted_ratings = user_predicted_ratings.sort_values(
            ascending=False)
        # get the top n movies
        user_predicted_ratings = user_predicted_ratings.head(n)
        # get movie name
        movieslist = movies.loc[movies['movieId'].isin(
            user_predicted_ratings.index), ['movieId', 'title']]

        # similarity = pd.DataFrame(user_similarity, index=users_crosstab.index, columns=users_crosstab.index)
        return movieslist["title"].tolist()

    else:
        return "User not found"


def user_base_recommender_using_KNNBaseline(user_id, n):

    # get the ratings that the user has not rated
    ratings_not_rated_by_user = ratings.loc[ratings['userId'] != user_id]

    data = Dataset.load_from_df(
        ratings_not_rated_by_user[['userId', 'movieId', 'rating']], reader)
    # cross_validate(KNNBaseline, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    trainset = data.build_full_trainset()
    KNNBaseline.fit(trainset)
    # sort the movies upon the highest accuracy of prediction
    ratings_not_rated_by_user['est'] = ratings_not_rated_by_user.apply(
        lambda x: KNNBaseline.predict(x['userId'], x['movieId']).est, axis=1)
    ratings_not_rated_by_user = ratings_not_rated_by_user.sort_values(
        by='est', ascending=False)
    # get the top n movies
    return movies_original.loc[movies_original['movieId'].isin(ratings_not_rated_by_user.head(n)['movieId'])]['title'].tolist()

# recommender function


def recommend(movie_name, n):
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    links = pd.read_csv('links.csv')
    # transform movie name to lower case for easier seach
    movies['title_lower'] = movies['title'].str.lower()
    ratings['rating_count'] = ratings.groupby('movieId')['rating'].sum()
    # keep only ratings that are rated by at least 10 users
    ratings = ratings[ratings['rating_count'] > 10]
    # Create a new dataframe with movieId, title and genres
    movies_df = movies.merge(ratings, on='movieId', how='inner')
    # popularity
    movies_df["popularity"] = movies_df["rating_count"]*movies_df["rating"]
    # splitting genres
    movies_df['genres'] = movies_df['genres'].str.split('|')
    if len(movies_df.loc[movies_df['title_lower'].str.contains(movie_name.lower())]) == 0:
        print(
            "Movie not in database. Please check your spelling. here are some popular rec")
        return movies_df.sort_values('popularity', ascending=False).head(n)["title"].tolist()
    else:
        genres = movies_df.loc[movies_df['title_lower'].str.contains(
            movie_name.lower())]['genres']
        movies_df = movies_df[movies_df['genres'].isin(genres)]
    # return movies_df.sort_values('popularity', ascending=False).head(n)
        return movies_df.sort_values('popularity', ascending=False).head(n)["title"].tolist()


def recommend_genre(genre, n):
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    # keep only ratings that are rated by at least 10 users
    ratings['rating_count'] = ratings.groupby('movieId')['rating'].sum()
    ratings = ratings[ratings['rating_count'] > 10]
    # Create a new dataframe with movieId, title and genres
    movies_df = movies.merge(ratings, on='movieId', how='inner')
    # popularity
    movies_df["popularity"] = movies_df["rating_count"]*movies_df["rating"]
    # splitting genres
    # movies_df['genres'] = movies_df['genres'].str.split('|')
    # choose the most popular movies of the genre

    movies_df = movies_df.loc[movies_df['genres'].str.contains(genre)]
    # return movies_df.sort_values('popularity', ascending=False).head(n)
    return movies_df.sort_values('popularity', ascending=False).head(n)["title"].tolist()


# def item_based_recommender(movie_name, n):

#     movies = movies_original.copy()
#     ratings = ratings_original.copy()
#     movies['title_lower'] = movies['title'].str.lower()
#     if len(movies.loc[movies['title_lower'].str.contains(movie_name.lower())]) == 0:
#         return "Movie not found"
#     else:
#         top_popular_for_movieId = movies.loc[movies['title_lower'].str.contains(
#             movie_name.lower())]['movieId'].values[0]

#         # # Create a new dataframe with movieId, title and genres
#         movies_df = movies.merge(ratings, on='movieId', how='inner')
#         # # Predator (1987) with movieId == 3527
#         # #sparse matrix
#         movies_crosstab_original = movies_df.pivot_table(
#             index='userId', columns='movieId', values='rating')
#         # movies_crosstab = movies_df.pivot_table(
#         #     index='userId', columns='movieId', values='rating')
#         movies_crosstab = movies_crosstab_original.copy()
#         predator_ratings = movies_crosstab[top_popular_for_movieId]
#         predator_ratings[predator_ratings >= 0]  # exclude NaNs
#         similar_to_predator = movies_crosstab.corrwith(predator_ratings)
#         # NaN means that no users rated both the movie and the predator
#         # drop the NaNs
#         corr_predator = pd.DataFrame(similar_to_predator, columns=['Viewer'])
#         corr_predator.dropna(inplace=True)
#         corr_predator.sort_values('Viewer', ascending=False)
#         rating = pd.DataFrame(ratings.groupby('movieId')['rating'].mean())
#         rating['rating_count'] = ratings.groupby('movieId')['rating'].count()
#         predator_corr_summary = corr_predator.join(rating['rating_count'])
#         predator_corr_summary.drop(top_popular_for_movieId, inplace=True)
#         top = predator_corr_summary[predator_corr_summary['rating_count'] >= 10].sort_values(
#             'Viewer', ascending=False).head(n)

#         return top.merge(movies, on='movieId', how='inner')[
#             ['title', 'genres', 'Viewer']]["title"].tolist()
