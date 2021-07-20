# If you want to repeat my work, you need to install this libraries:
# 1. Open cmd
# 2. Paste: pip install requests to download requests library.
# 3. Make second step for other 2 libraries
# 4. Use this code and note, that it makes a .csv file in the end of the work

# Import all needed libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# This variable is responsible for changing IMDb pages: 1-100 page, 101-200 page and so on...
# I made it -99 to increase it by 100 in every while step
start = -99

# Making a Pandas data frame to insert the ratings data
df = pd.DataFrame(columns=['PlaceInRating',
                           'Grade',
                           'Name',
                           'Year',
                           'LengthInMinutes',
                           'Genre',
                           'Votes',
                           'GrossIn$',
                           'MetaScoreRating',
                           'MovieDescription',
                           'Directors',
                           'Stars'])

# This is a main while loop of parsing the IMDb rating.
# Variable 'start' is responsible for a payload instruction 'start'
# That is responsible in get request for a page that i'm trying to open
while start <= 1000:  # There is no info after 1000 :)
    start += 100  # Increasing this variable to go to the next page of rating
    url = 'https://www.imdb.com/search/title/'  # An immutable part of url
    headers = {"Accept-Language": "en-US,en;q=0.5"}  # Header "Accept-Language" to get info in english, not in russian

    if start <= 1:  # handling with first page
        # https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_prv
        payload = {'groups': 'top_1000',
                   'sort': 'user_rating,desc',
                   'count': 100,
                   'ref_': 'adv_prv'}
    else:
        # https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=101&ref_=adv_nxt
        payload = {'groups': 'top_1000',
                   'sort': 'user_rating,desc',
                   'count': 100,
                   'start': start,
                   'ref_': 'adv_prv'}

    # Get HTML text of a page using requests method get()
    # and our params: payload and headers
    data = requests.get(url, params=payload, headers=headers).text

    # Parsing of data HTML string using BeautifulSoup
    soup = BeautifulSoup(data, 'html5lib')

    # 100 elements on each page
    # I confess that my methods of parsing webpages are not great at all, i am learning right now :D
    # All 100 rows were 'div' tags with 'lister-item mode-advanced' class, so i decided to find them
    # using exactly this information
    ratings = soup.find_all('div', class_="lister-item mode-advanced")

    # Parsing of all 100 movies on the page
    # 'film' - certain movie, 'ratings' - all 100 movies on a page
    for film in ratings:
        # 'info' - most informative 'div' tag, which contains all info that i need
        info = film.find('div', class_="lister-item-content")

        # 6 rows below are products of pure magic of BeautifulSoup
        # WARNING: it looks ugly and not only looks :)
        # strip() -> delete all spaces before and after string
        place_in_rating = int(info.find(class_='lister-item-index unbold text-primary').text.strip()[:-1].replace(',', ''))
        name = info.find('h3').find('a').text.strip()
        year = int(info.find(class_="lister-item-year text-muted unbold").text.strip()[-5:-1])
        length = int(info.find(class_="runtime").text.strip().split(' ')[0])
        genre = info.find(class_="genre").text.strip()
        grade = float(info.find(class_="ratings-bar").find(class_="inline-block ratings-imdb-rating").find('strong').text.strip())

        # This try-except block is dedicated to parsing MetaScore rating of the film
        # Some films don't have this rating, so i place None
        try:
            meta_score_rating = int(info.find(class_="inline-block ratings-metascore").find('span').text.strip())
        except:
            meta_score_rating = None

        # Brief description of the movie
        description = info.find_all('p', class_="text-muted")[1].text.strip()

        # I faced a little problem: some movies have 2+ directors or stars
        # So i parsed all of them using simple code below:
        directors_and_stars = info.find_all('p')[2].find_all()  # All 'p' tags that contain info about both movie directors and stars
        directors = ''  # Here i will append all directors of the movie
        stars = ''  # Here i will append all stars of the movie
        isTrue = False  # Boolean value to switch from directors to stars
        for elem in directors_and_stars:  # Examine all elements in directors_and_stars
            if elem.name == 'span':  # If it's a 'span' tag, which contains only ghost '|' symbol - time to switch
                isTrue = True
                continue
            if isTrue == False:  # If there is still no '|' - we append directors to the 'directors'
                directors += elem.text.strip()
                directors += ', '  # Making some beauty
            else:  # Else - we append stars to the 'directors'
                stars += elem.text.strip()
                stars += ', '  # Making some beauty
        directors = directors[:-2]  # Delete ', ' at the end of the string
        stars = stars[:-2]  # Delete ', ' at the end of the string

        # Information about votes and gross of film is placed into two tags
        # Which both have unique attribute: "name" - <span name="nv" ...>, <span name="nv" ...>
        votes_and_gross = info.find_all(attrs={"name": "nv"})
        votes = int(votes_and_gross[0].text.strip().replace(',', ''))  # I extract votes info into 'int' value
        # One more try-except block to get info about gross of the movie
        # Reason is the same as in MetaScore rating - sometimes movie doesn't have gross or there is no info about it
        try:
            gross = int(float(votes_and_gross[1].text.strip()[1:-1]) * 1000000)  # Multiply it by 1.000.000 to get certain amount of US Dollars
        except:
            gross = None  # If no gross info - place None into 'gross' value

        # The last step - append information about 1 film into Pandas data frame.
        # Appending info like a Python dictionary: corresponding values to corresponding keys:
        df = df.append({'PlaceInRating': place_in_rating,
                        'Grade': grade,
                        'Name': name,
                        'Year': year,
                        'LengthInMinutes': length,
                        'Genre': genre,
                        'Votes': votes,
                        'GrossIn$': gross,
                        'MetaScoreRating': meta_score_rating,
                        'MovieDescription': description,
                        'Directors': directors,
                        'Stars': stars
                        }, ignore_index=True)

    # Information to calm yourself and keep abreast of events
    # Don't be scared when you see 'Parsed: 1001 - 1101' - this is a feature!
    print('Parsed:', start, '-', start + 100)


# Uploading information to the 'movie_rating.csv' file
df.to_csv('movie_rating.csv', index=False)

# The end.
# Thanks for reading and scrolling this file.
# My github repository of this .py file:
