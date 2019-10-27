"""Gets quotes"""

class Quote(object):
    pass

class Motivational(Quote):
    def __init__(self):
        self.quote = 'You are alive, that is pretty OK!'
        self.by = 'Unknown'

    def get(self):
        return "\"{}\" – {}".format(self.quote, self.by)

    def get_new(self):
        # TODO: Get this from the internets
        pass