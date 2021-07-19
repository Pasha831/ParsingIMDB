import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&view=advanced'
data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')
# print(soup.prettify())

# 50 elements on each page
ratings50 = soup.find_all('div', class_="lister-item mode-advanced")

# making a Pandas dataframe to insert the ratings data
df = pd.DataFrame(columns=['PlaceInRating', 'Grade', 'Name', 'Year', 'LengthInMinutes', 'Genre', 'MetaScoreRating', 'MovieDescription', 'Directors', 'Stars', 'Votes', 'GrossInMillions$'])

for film in ratings50:
    info = film.find('div', class_="lister-item-content")

    place_in_rating = int(info.find(class_='lister-item-index unbold text-primary').text.strip()[:-1])
    name = info.find('h3').find('a').text.strip()
    year = int(info.find(class_="lister-item-year text-muted unbold").text.strip()[-5:-1])
    length = int(info.find(class_="runtime").text.strip().split(' ')[0])
    genre = info.find(class_="genre").text.strip()
    grade = float(info.find(class_="ratings-bar").find(class_="inline-block ratings-imdb-rating").find('strong').text.strip())

    try:
        meta_score_rating = int(info.find(class_="inline-block ratings-metascore").find('span').text.strip())
    except:
        meta_score_rating = 'unknown'
    description = info.find_all('p', class_="text-muted")[1].text.strip()

    directors_and_stars = info.find_all('p')[2].find_all()
    directors = ''
    stars = ''
    isTrue = False
    for elem in directors_and_stars:
        if elem.name == 'span':
            isTrue = True
            continue
        if isTrue == False:
            directors += elem.text.strip()
            directors += ', '
        else:
            stars += elem.text.strip()
            stars += ', '
    directors = directors[:-2]
    stars = stars[:-2]

    votes_and_gross = info.find_all(attrs={"name": "nv"})
    votes = votes_and_gross[0].text.strip()
    try:
        gross = int(float(votes_and_gross[1].text.strip()[1:-1]))
    except:
        gross = 'unknown'


    df = df.append({'PlaceInRating':place_in_rating,
                    'Grade':grade,
                    'Name':name,
                    'Year':year,
                   'LengthInMinutes':length,
                   'Genre':genre,
                   'MetaScoreRating':meta_score_rating,
                   'MovieDescription':description,
                   'Directors':directors,
                   'Stars':stars,
                   'Votes':votes,
                   'GrossInMillions$':gross}, ignore_index=True)


df.to_csv('movie_rating.csv', index=False)
