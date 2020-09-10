from app import app
import urllib.request ,json
from app.models import movies

Movie = movies.Movie



#getting the API key
api_key = app.config['MOVIE_API_KEY']

#getting the moviebase url
base_url = app.config['MOVIE_API_BASE_URL']



def get_movies(category):
    '''
    function to get the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)
        
        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)
            
    return movie_results

def get_one_movie(id):
    '''
    function to get movie by its id
    '''
    get_movie_details_url = base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)
        
        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')
            
            movie_object = Movie(id,title, overview, poster, vote_average, vote_count)
    return movie_object 

def search_movie(movie_name):
    '''
    function to search a movie from the movie list
    '''
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)
        
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)
            
    return search_movie_results

def process_results(movie_list):
    '''
    function that processes the list of movie details to movie objects
    Args:
        movie_list: Alist of dictionaries that contain movie details
    returns: 
        movie_results: A list of movie objects
    '''
    
    movie_results = []
    
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        
        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)
            
    return movie_results