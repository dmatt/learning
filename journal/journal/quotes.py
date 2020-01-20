"""Gets quotes"""
from requests import request

class Quote(object):
    pass

class Motivational(Quote):
    def __init__(self):
        # Default fallback quote
        self.quote = 'You are alive, that is pretty OK!'
        self.by = 'Unknown'
        # Attempt to get a random quote
        self.get_from_internet()

    def get_from_internet(self):
        try:
            req = request('GET', 'https://quotes.rest/qod').json()
            self.quote = req['contents']['quotes'][0]['quote']
            self.by = req['contents']['quotes'][0]['author']
        except Exception as e:
            print('Could not get a quote: {}'.format(e))

    def __str__(self):
        return "\"{}\" – {}".format(self.quote, self.by)