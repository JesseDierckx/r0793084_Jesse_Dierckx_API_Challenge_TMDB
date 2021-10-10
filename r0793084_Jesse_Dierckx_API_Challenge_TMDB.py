# all the modules that you need to import so the script works.
import urllib.parse
import requests
from tabulate import tabulate

#start to create variables and fill in read access tokens.
api = "https://api.themoviedb.org/3/" # base url to connect to the api.
bearer = "" # put your own oauth 2.0 bearer token in this parameter slot.
headers = {'Authorization': 'Bearer ' + bearer}
film = "" # the parameter that you will fill in to search for a particular film.
# upper 2 lines are for connecting to the api with a bearer token.
while film != "q" or film != "quit":
    film = input("What movie do you wanna watch? (q)uit :")
    if film == "q" or film == "quit":
     break
    # the url is compromised from the baseurl + the search function with the title as parameter of the movie you wanna watch.
    url = api + "search/movie?" + urllib.parse.urlencode({"query":film})
    # here we print the url that is needed to get the necessary information from the api.
    print(url + "\n")
    # this line pulls the data from the api so we can display it.
    data = requests.get(url,headers=headers).json()
    # a list with all the results gets made every time you put in a new parameter.
    movies = []
    # for every result that you get it is added to the list.
    for result in data["results"]:
        movies.append([result["title"], result["popularity"], result["release_date"], result["id"]])
    # through tabulate the results get printed in a table.
    # this line tells you if the movie you typed, does not exist or isn't found.
    if movies == []:
        print('sorry, no films found that have this name')
    # if it finally falls to the else under here the table gets displayed and compartmentalized.
    else:
        print(tabulate(movies, headers=["film", "popularity", "release date", "id"]))