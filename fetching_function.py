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


def get_movie_img(movie_name):

    url = "https://online-movie-database.p.rapidapi.com/title/find"

    querystring = {"q": f'{movie_name}'}
    # querystring = {"q": 'the avengers'}

    headers = {
        "X-RapidAPI-Key": "639b12a7a5msh373ca3c1d141b4ep19e107jsn6ae77a65c491",
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    res = response.json()
    # get picture url
    return res["results"][0]["image"]["url"]
