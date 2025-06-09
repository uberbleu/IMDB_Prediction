# IMDB_Prediction

## Intro

In this project, we will explore the intricate relationships between movie genres, box office performance and other factors that can turn a modest flick into a blockbuster hit.
* Full notebook: https://colab.research.google.com/drive/1Db92SfDaxB2XtxYGtk3yIaXW9bfAuZKl?usp=sharing

## 1. Problem Definition

In a statement, can we identify the key factors that influence a movie's success by examining how genres, budgets, and box office performance affect IMDb ratings?
Will analyzing these variables help us determine what makes a film a hit or a miss, providing valuable insights for film production and distribution strategies?

## 2. Data

Full data: https://drive.google.com/file/d/11qxJVSnIIOC6MiIZl6b0zwJ3gXiZCUGv/view?usp=sharing

## 3. Evaluation

Can we identify at least two key factors that significantly influence a movie's box office success and IMDb rating?

## 4. Features

* Poster_Link: URL link to the movie's poster image.
* Series_Title: The title of the movie or series.
* Released_Year: The year the movie was released.
* Certificate: The rating or certification of the movie (e.g., PG, R).
* Runtime: The duration of the movie in minutes.
* Genre: The genre(s) of the movie (e.g., Action, Drama).
* IMDB_Rating: The movie's rating on IMDb.
* Overview: A brief summary of the movie's plot.
* Meta_score: The movie's score on Metacritic.
* Director: The director of the movie.
* Star1: The first main actor or actress in the movie.
* Star2: The second main actor or actress in the movie.
* Star3: The third main actor or actress in the movie.
* Star4: The fourth main actor or actress in the movie.
* No_of_Votes: The number of votes the movie has received on IMDb.
* Gross: The total box office gross revenue of the movie.

## Conclusions
1. The average movie duration for highly rated movies is 123 min.
2. Frank Darabont makes the highest rated movies.
3. 2020 has the most outliers when it comes to highly rated movies (in a positive way).
4. Runtime has a positive relationship with the IMDB rating but no relationship with meta score.
5. Either people prefer recent movies or recent movies have higher quality.
6. In the decade of 2020, a highly rated movie is expected to earn above 100M.

## Retrospective
## 1. Have we met our goal?
We have met our goal by identifying "Gross_mil" and "Decade" as key variables influencing movie success. The analysis shows that gross revenue and the decade of release significantly affect a movie's financial performance, providing insights into how these factors contribute to a film's success over time.

## 2. What did we learn from this experience?
We learned that a movie's financial success is strongly influenced by its gross revenue and the era in which it was released, highlighting the importance of these factors in predicting a film's box office performance. 

Additionally, our analysis of trends across decades and the correlation between different variables provides valuable insights into the evolving dynamics of the movie industry.

## 3. What are some future improvements?
Future improvements could include incorporating additional variables such as marketing budgets or audience demographics to gain a more comprehensive understanding of movie success. 
Additionally, applying advanced machine learning techniques to predict box office performance could enhance the accuracy and depth of the analysis.
