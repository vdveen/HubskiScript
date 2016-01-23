import requests
from operator import itemgetter

class Hubski:
    def __init__(self):
        self.base_url = "https://api.hubski.com"

    def get_pub(self, id):
        pub = requests.get(self.base_url + "/publication/" + str(id), 
                           verify=False).json()
        if pub:
            return Publication(pub)
        return None

class Publication(object):
    def __init__(self, response):
        self.__dict__ = response

    def sortByVote(self, reverse=False):
        return sorted(self.votes, key=itemgetter('id'), reverse=reverse)

    def __repr__(self):
        return "<Publication ID={}, user={}, domain={}>"\
                  .format(self.id, self.user, self.domain)
