# ParsingIMDb
My name is Pasha.

I am learning Data Science on Coursera site and have some free time to practice with parsing web sites.

Here i am parsing <a href='https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_nxt'>IMDb raiting</a> - 1000 top films of all the time.

<img src="https://vgif.ru/gifs/157/vgif-ru-28496.gif" width="200" height="200" />
<hr>

## Objectives:
* earn experience in parsing web pages
* earn experience in Data Science
* get some basics of Data Science analytics
* try to visualize data that i will get
* try to tell you a brief story on the insights i'll get

**Fasten seat belts, we take off!**

<img src='https://lh3.googleusercontent.com/proxy/1qpBNy2x1OCJoCBs7I8D502iQ1deECPR-1456ri2f5-B5KoiSYIhbyrnu_xbnBMdgClsBbZjvB7JElp54rK9hr-wFxQocA8z3KUdb-VX-40ynARTHmQpkr68lMChVtpt' width="400" height="300">


<hr>

## Getting started
First of all, i found a great IMDb database about Top-1000 films in human history.

![image](https://user-images.githubusercontent.com/46136468/126282645-a93e6d7a-73b1-4b82-a711-b2d4b56a05b0.png)


I chose it because it was:
* easy to parse *(but not always :D)*
* easy to understand
* easy to make a stories based on result of this database

**Significant notes:**
* this dataset can be not representative too much, because it contains only 1000 best films, not all movies in history
* this dataset sometimes contains empty cells, because some info like Metascore score of films' gross are really unknown

<img src='https://www.meme-arsenal.com/memes/b95277c152527c3379654dced767edcb.jpg' width="400" height="300">

## Steps of work
I've parsed it in my .py file making these steps (*read comments to understand, what the h#ll is going on?*):
1. import libraries such as **Pandas**, **BeautifulSoup** and **Requests** to handle with data
2. **made a request** to IMDb site to get text version of this page
3. parsed all **1000 rows** of a table
4. extarct useful info into a **Pandas dataframe**
5. export dataframe data **to .csv** file to read and to work with it later

*P.S.: I used a while loop to parse this page, because this raiting consits of **10 different pages***

After all this work, i have a litle 1000-films dataset, which have these columns:

![image](https://user-images.githubusercontent.com/46136468/126227948-85c55de5-ac1c-4f43-ae29-76f77ef3a17b.png)

and looks like this:

![image](https://user-images.githubusercontent.com/46136468/126286046-685b9a57-4aa5-43c5-947c-bea1ab34138e.png)


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

<img src='https://vgif.ru/gifs/138/vgif-ru-15976.gif' width="400" height="300">

## Analyzing the data
Here we are going to tell about all 7 (or more questions), using my ability to tell stories and making graphs (which now is not really good 😟)

Let's explore answer to start some simple questions.

For exmaple, what are **10 best films in history**?:

![image](https://user-images.githubusercontent.com/46136468/126324184-dfa928ab-0da8-4c9e-89c6-440998ec1922.png)

<img src='https://lh3.googleusercontent.com/proxy/ywidB_H5LKokUzDvWXoxjQNKsJsT7ysF4zqXQ_K1Kx_XsYMoatapH2-51Nm-fnwqy-9gtY44DWuk9-oDlfaojwFuX8_HdAVFbXBAg2lYOio7OR0DFL_Mf9q3cvabRdd-2whp3rB0G0T5PHrgC7FI5RoTXs4HEQ' width="400" height="300">

## How to contact me?
<img src='https://99px.ru/sstorage/86/2016/12/image_860612160048418882106.gif' width="80" height="60">Me in Telegram: *https://t.me/nightshift48*

<img src = 'https://i.ytimg.com/vi/ih85LYvbDEM/maxresdefault.jpg'>
