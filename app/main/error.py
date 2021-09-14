from flask import render_template

from . import main

@main.errorhandler(404)
def errorpage(error):

    '''
    This function renders the 404 error page
    '''

    return render_template('404.html', error=error), 404