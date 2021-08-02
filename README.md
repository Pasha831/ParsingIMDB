# ParsingIMDb
My name is Pasha.

I am learning Data Science on Coursera site and have some free time to practice with parsing web sites.

Here i am parsing <a href='https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_nxt'>IMDb raiting</a> - 1000 top films of all the time.

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/scary.gif' width=600>
<hr>

## Objectives:
* earn experience in parsing web pages
* earn experience in Data Science
* get some basics of Data Science analytics
* try to visualize data that i will get
* try to tell you a brief story on the insights i'll get

**Fasten seat belts, we take off!**

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/clever.jpg'>


<hr>

## Getting started
First of all, i found a great IMDb database about Top-1000 films in human history.




I chose it because it was:
* easy to parse *(but not always :D)*
* easy to understand
* easy to make a stories based on result of this database

**Significant notes:**
* this dataset can be not representative too much, because it contains only 1000 best films, not all movies in history
* this dataset sometimes contains empty cells, because some info like Metascore score of films' gross are really unknown

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/working_cat.jfif' height=300>

## Steps of work
I've parsed it in my .py file making these steps (*read comments to understand, what the h#ll is going on?*):
1. import libraries such as **Pandas**, **BeautifulSoup** and **Requests** to handle with data
2. **made a request** to IMDb site to get text version of this page
3. parsed all **1000 rows** of a table
4. extarct useful info into a **Pandas dataframe**
5. export dataframe data **to .csv** file to read and to work with it later

*P.S.: I used a while loop to parse this page, because this raiting consits of **10 different pages***

After all this work, i have a litle 1000-films dataset, which have these columns:

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/columns_in_rating.png'>

and looks like this:

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/table_example.png'>

There are some rows with *None values*, in some cases i will remove them to make everything clear.

<hr>

<img src='https://ichef.bbci.co.uk/news/640/cpsprodpb/5CB0/production/_99782732_37e58b7e-9cf4-44e0-86c7-59c42f34697a.jpg' width="400" height="300">

Need to mention, that i am learning on **<a href='https://www.coursera.org/'>Coursera</a>** and in process to get my **<a href='https://www.coursera.org/professional-certificates/ibm-data-science'>IBM Data Science Professional Certificate</a>** (5/10 courses done)

Therefore, i often used instruments from **IBM Cloud** like **Watson Studio** or **Services to work with Database**.

## What am i going to do now?
That's a good question and i have some answers for you.

Here is the small list of inforamtion, that i want extract from data which i obtained:
1. What are the best movies?
2. Which era was the most eventful in the film industry?
3. Which era of film indusrty was teeming with profits?
4. How is changing length of the film during years?
5. How is changing gross of the film during years?
6. What realtionship between length of the film and the year when it was created?
7. Is there any relationship between length of the name of the film and gross sums or rating of film?

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/surprise.gif' width="400" height="300">

## Analyzing the data
Here we are going to tell about all 7 (or more questions), using my ability to tell stories and making graphs (which now is not really good 😟)

Let's explore answer to start some simple questions.

## **10 best movies in history**

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/10_best_films.png'>

As you can see, the most raited film in history (by IMDb of course) - **The Shawshank Redemption**. 
In my opinion, this movie is really cool and all, 
but i'm agree with MetaScore raiting (80 credits) 
and i **would put** this movie **below** in raiting. 
My first place is a **'1+1'** movie.

Next films in the top three are **The Godfather** (
film, that i will watch soon in English, therefore 
can't put any my words here) 
and **Soorarai Pottru** 
(something from India as i understand, maybe this movies is great, 
but Indian indusrty - not in my taste.

## **Frequency of cinematography releases by years**

<img src ='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/film_production.png'>

Second chart is going to show us frequency of cinematography releases by years.
Exploring it, we can recognize some interesting features:

1. Film production in the world since 1920's (the oldest films in our data set)
is **always growing in sizes**.
   
2. We can find some **peaks** on the chart:
    * Fist peak dated **1939-1941**. It is the time, when
    American cinema was significantly filled with 
    superhero comics from **Marvel and DC**. Also there were a lot of
    films about **WW2**.
    * The best year in film production, which is full of good films
    that are in IMDb rating - **2004**. There were filmed 33 films.
      
3. We can see a sad story at **2020**. With the advent of coronavirus movie
   industry rapidly died. There were only **8** films which hit the IMDb raiting:
   * Soorarai Pottru
   * Dara of Jasenovac
   * Hamilton
   * Demon Slayer: Mugen Train
   * The Father
   * Soul
   * The Trial of the Chicago 7
   * Another Round
    
In conclusion, movie production was developing gradually and I can't note period of time when film industry was "on fire".


## Average incomes by movies by year of production
Let's find mean value for each year and examine this plot.

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/gross.png'>

In my opinion, there are 5 interesting outliers among all years: 1939, 1956, 1965, 1977 and 2018 years. Let's see three most
successful films in each year:

1. 1939 - **70.120.000** $
   * Mr. Smith Goes to Washington - 9.600.000 $
   * Gone with the Wind - 198.680.000 $
   * The Wizard of Oz - 2.080.000 $
   

2. 1956 - **93.740.000** $ and only one film in rating
   * The Ten Commandments - 93.740.000 $


3. 1965 - **96.000.000** $
   * For a Few Dollars More - 15.000.000 $ 
   * The Sound of Music - 163.210.000 $
   * Doctor Zhivago - 111.720.000 $ (*I didn't know that there is a movie about this book with such grosses!*)


4. 1977 - **164.000.000** $
   * Star Wars: Episode IV - A New Hope - 322.740.000 $ (*predictable*)
   * Annie Hall - 39.200.000 $
   * Close Encounters of the Third Kind - 132.090.000 $


5. 2018 - **186.000.000** $ (*let's see five of them* :D )
   * Avengers: Infinity War - 678.820.000 $
   * Incredibles 2 - 608.580.000 $
   * Deadpool 2 - 324.590.000 $
   * Mission: Impossible - Fallout - 220.160.000 $
   * Bohemian Rhapsody - 216.430.000 $

2018 was full of great films with great grosses!

But which movie has the highest box office? *drumroll...*

This movie is **Star Wars: Episode VII - The Force Awakens** with 936.660.000 $ box office.
Please, don't throw tomatoes at me! I know that "Avatar" has **2.798.579.794** $, but this film isn't in movie rating D:

IMDb rating includes only Gross US & Canada, and that's a bullshit! 
(*You can see worldwide box office, but only checking appropriate page of film,
that is very costly in parsing*)


## Length of films

Let's see another plot:

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/length.png'>

We can see, that there is no year dependence for average length of movies.

Telling you exact number of average length - it is **123** minutes.

Let's get acquainted with the shortest and the longest movie:

* The shortest - Sherlock Jr., **45** minutes
* The longest - Gangs of Wasseypur, **321** minutes, or 5 hours and 21 minutes!!! 
  (*chance of falling asleep while watching it - about 99.9999%*)


## Discovering realtionships between features
Let's imagine that we are film producers. Our aim - create great film
which must please people. And of course, we want to make money!

Therefore, we want (*everyone has their own order*):
1. **Big grades** from people
2. **Much money** from people

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/leo_gif2.gif'>

In this section, we will use **scatter plots with regression line** -
 the best way to find relationships between different features.

You can easily see relationship between two different features on this plot.
In addition to it, I am going to prove the relationship using 
<a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html?highlight=corr#pandas.DataFrame.corr"> correlation score </a>
from *Pandas*.

Briefly, linear relationships between two variables can be 
* positive (+1)
* negative (-1)
* no relationship (0)

For instance: 
* **more** cat photos -> **more** happiness (positive relationship)
* **more** suicidal guys -> **less** suicidal guys (negative relationship)
* **more** photo of bears -> my level of happiness won't increase (no relationship, it doesn't matter to me)

Here we have a table, that represents relationships between grade
of film and other attributes:

| Factor        | Correlation score           | Brief explanation  |
| ------------- |:-------------:| -----:|
|  Place in rating    | -0.939748 | The further we are from the beginning of the rating, the further we are from good ratings, it's logical |
| Year      | -0.122696      |  Practically no relationship between them  |
| Length in minutes | 0.237634      |    Still not the biggest correlation score, but there is a *small impact* on grade of film |
|Votes|0.472281|More interesting information: more votes has the movie - higher the score|
|Gross in $|0.088599|Almost no relationship between box office of movie and it's rating|
|Metascore rating|0.266656|Weak relationship: bigger Metascore rating - higher grade|

Let's see some plots of these relationships:

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/rel_grade.png'>

<hr>

Now let's create the same table and plots for explore relationship between
box office of movie and other attributes:

| Factor        | Correlation score           | Brief explanation  |
| ------------- |:-------------:| -----:|
|  Place in rating    | -0.060560 | Place in rating doesn't impact on box office of the movie |
| Year      | 0.236329      |  We have weak relationship: the newer the movie - the more revenue |
| Length in minutes | 0.142009      |Really small relationship|
|Votes|0.578388|Another interesting information: more votes has the movie - higher the box office (it's logical too: everyone who voted watched the movie :D|
|Grade|0.088599|Almost no relationship between box office of movie and it's rating|
|Metascore rating|-0.039374|No relationship|

And here we have some plots about this:

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/rel_gross.png'>


## Making predictions
I think that it would be cool to **predict box office of a movie** before its out on screens. Knowing your box
office is incredible ability - you can predict your proceeds from each movie.

Let's predict box office on this information:
* Year of production
* Length in minutes
* Quantity of votes
* Metascore rating
* Length of movie title (it's going to be interesting!)
* Length of movie description (the same case as above)

Two last parameters are really crazy! Let's explore relationship where
it seems that there is no relationship at all.

I'm going to use <a href='https://scikit-learn.org/stable/'>sklearn</a> library and linear regression
with parameters above. So let's get started!

First, we have to drop all null rows in table and also columns, where rows of it are not
integers (like "Name" or "Description" columns).

Then, add columns "NameLen" and "DescLen" (last two parameters of our plan).

After all, import ```sklearn``` library and make ```LinearRegression()``` object to fit our model and
make predictions.

Now, we have an expression for calculating the box office of a movie:

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/equation.jpg'>

Where X1, X2, X3 ... X6 - **coefficients** for each parameter (*all of them after
standardization are between 0 and 1*) and first number is and **intercept**.

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/distrib.png'>

Plot above show us how our model predicts the box office. Honestly, I'm surprised!
It's very close to reality. Maybe let's try it?

There is a movie "Soorarai Pottru", which was dropped from our training data,
because it didn't have box office information (*film is very young, check its box office later and compare with prediction below!*). This will be our test subject.

Information about movie to predict box office:
* Year of production: 2020
* Length in minutes: 153
* Quantity of votes: 84950
* Metascore rating: 78 (it's actually none, so I replaced none with average Metascore rating)
* Length of movie title: 15 
* Length of movie description: 177

Prediction is **61.786.495** $. It's pretty real! Check it when information
about box office of this movie will appear.

<hr>

I'm going to try with one more movie: "It's a Wonderful Life". We don't know box office of this movie
using IMDb raiting but i found that gross:
* in US & Canada - $44,000
* worldwide - $6,184,298

Let's do the same work such as with previous film:
* Year of production: 1946
* Length in minutes: 130
* Quantity of votes: 415284
* Metascore rating: 89
* Length of movie title: 21
* Length of movie description: 144

And prediction for this film is - **55.223.171** $. Hah, it's almost $6.184.298, right?
Here we see, that our model sometimes is bad at predictions...

<hr>

The last one for this time - "Hamilton" movie (2020, it's fresh and don't have info about box office).
Necessary information:
* Year of production: 2020
* Length in minutes: 160
* Quantity of votes: 68685
* Metascore rating: 90
* Length of movie title: 8
* Length of movie description: 208

The last prediction for today - 57.355.346 $. We will check it in near future..;

## Conclusion
You can easily f#ck the world using information and Data Science skills! **Stay curious**.

> Tell a great story from your analyzises. Not like me :D

## How to contact me?
<a href="https://t.me/nightshift48">Me in Telegram</a> 

<a href="https://vk.com/notuselessman">Me in VK</a>

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/japanese_cat.jfif'>
