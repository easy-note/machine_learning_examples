import pandas as pd
import os

movie = pd.read_csv('../data/movie.csv')
movie = movie.loc[:,["movieId","title"]]

rating = pd.read_csv('../data/rating.csv')
rating = rating.loc[:,["userId","movieId","rating"]]

data = pd.merge(movie, rating) # shape : [20000263 rows x 6 columns]
data = data.iloc[:1000000,:]

pivot_table = data.pivot_table(index=['userId'], columns=['title'], values='rating')
print(pivot_table.head(10))

movie_watched = pivot_table['Bad Boys (1995)']
similarity_with_other_movies = pivot_table.corrwith(movie_watched)
print(similarity_with_other_movies)