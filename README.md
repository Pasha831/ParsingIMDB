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

<hr>

<img src='https://ichef.bbci.co.uk/news/640/cpsprodpb/5CB0/production/_99782732_37e58b7e-9cf4-44e0-86c7-59c42f34697a.jpg' width="400" height="300">

Need to mention, that i am learning on **Coursera** and in process to get my **IBM Data Science Professional Certificate** (5/10 courses done)

Therefore, i often used instruments from **IBM Cloud** like **Watson Studio** or **Services to work with Database**.

## What am i going to do now?
That's a good question and i have some answers for you.

Here is the small list of inforamtion, that i want extract from data which i obtained:
1. Is there any relationship between length of the name of the film and gross sums or rating of film?
2. Which era was the most eventful in the film industry?
3. Which era of film indusrty was teeming with profits?
4. How much films were created each year? (is there any areas of decline or growth of the industry?)
5. How is changing length of the film during years?
6. How is changing gross of the film during years?
7. Whats the realtionship between length of the film and the year when it was created?
8. more questions will appear in future 😅

<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/surprise.gif' width="400" height="300">

## Analyzing the data
Here we are going to tell about all 7 (or more questions), using my ability to tell stories and making graphs (which now is not really good 😟)

Let's explore answer to start some simple questions.

## **10 best movies in history**

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/10_best_films.png'>

As you can see, the most raited film in history (by IMDb of course) - **The Shawshank Redemption**. In my opinion, this movie is really cool and all, but i'm agree with MetaScore raiting (80 credits) and i **would put** this movie **below** in raiting. My first place is a **'1+1'** movie.

Next films in the top three are **The Godfather** (film, that i will watch soon in English, therefore can't put any my words here) and **Soorarai Pottru** (something from India as i understand, maybe this movies is great, but Indian indusrty - not in my taste.

## **Frequency of cinematography releases by years**

## How to contact me?
<img src='https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/crying_DiCaprio.gif' width="80" height="60">Me in Telegram: *https://t.me/nightshift48*

<img src = 'https://github.com/Pasha831/ParsingIMDB/raw/main/cats_and_screenshots/japanese_cat.jfif'>
