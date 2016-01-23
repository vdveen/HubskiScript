import requests
from operator import itemgetter

class Hubski:
    def __init__(self):
        self.base_url = "http://api.hubski.com"

    def get_pub(self, id):
        pub = requests.get(self.base_url + "/publication/" + str(id)).json()
        return Publication(pub)

class Publication(object):
    def __init__(self, response):
        self.__dict__ = response

    def sortByVote(self, reverse=False):
        return sorted(self.votes, key=itemgetter('id'), reverse=reverse)
