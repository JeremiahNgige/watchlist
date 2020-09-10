import unittest
from models import movies
Movie = movies.Movie

class TestMovie(unittest.TestCase):
    '''
    Test behaviour of movies class
    '''
    def setUp(self):
        '''
        setup a method that will run befoe every test
        '''
        self.new_movies = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movies,Movie))
        
    def test_movie(self):
        self.assertEqual(self.new_movies,
            self.new_movies)
        
if __name__ == '__main__':
    unittest.main()