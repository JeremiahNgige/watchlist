from flask import render_template
from app import app

@app.errorhandler(404)
def error_page(error):
    '''
    view function to respond with our custom error page
    '''
    return render_template('error.html'),404