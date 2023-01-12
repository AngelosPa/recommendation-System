#import requests
import requests
# imdb movies api
# url = "https://online-movie-database.p.rapidapi.com/title/get-details"
# querystring = {"tconst": "tt0944947"}
# headers = {
#     "X-RapidAPI-Key": "eafd80d964msh84d79dbf75cdb6bp18fef8jsn333a4d75cd6f",
#     "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
# }
# response = requests.request("GET", url, headers=headers, params=querystring)
# res = response.json()
# # get picture url
# print(res["image"]["url"])


def get_movie_info(movie_name):

    url = "https://online-movie-database.p.rapidapi.com/title/find"

    # querystring = {"q": f'{movie_name}'}
    querystring = {"q": 'the avengers'}

    headers = {
        "X-RapidAPI-Key": "eafd80d964msh84d79dbf75cdb6bp18fef8jsn333a4d75cd6f",
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)
    print(get_movie_info("the avengers"))
