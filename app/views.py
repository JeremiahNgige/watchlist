from flask import Flask,render_template,request,redirect,url_for
from app import app
from .request import get_movies, get_one_movie, search_movie

@app.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    search_movie = request.args.get('movie_query')
    
    
    #getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    print(popular_movies)
    title = 'Home - Welcome to the best movie review website Online'
    if search_movie:
        return redirect(url_for('search', movie_name=search_movie))
    else:
        return render_template('index.html',title=title,popular_movies=popular_movies,
                                upcoming_movie=upcoming_movie, now_showing_movie=now_showing_movie
                                )
    
@app.route('/movie/<int:id>')
def movie(id):
    '''
    view movie function that returns the movie details
    '''
    movie = get_one_movie(id)
    title = f'{ movie.title }'
    
    return render_template('movies.html',title=title,movie=movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    view function to render our searched movie
    '''
    movie_name_list = movie_name.split(" ")    
    movie_name_format = "+".join(movie_name_list)   
    searched_movies = search_movie(movie_name_format)
    
    return render_template('search.html',searched_movies=searched_movies)