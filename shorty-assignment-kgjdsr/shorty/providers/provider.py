from urllib import request
from shorty.providers.bitly.bitly_url import *
from shorty.providers.tinyurl.tiny_url import *

# The class Provider is responsible for shortening the url based on the provider given in the input

class Provider:

    def __init__(self, request):
        if 'provider' in request:   
            provider = request['provider']

        self.provider = provider.lower()

        self.url = request['url']
    
    # The short function shorts the url and returns the shortened result
    def short(self):
        self.link = None
        if self.provider == 'tinyurl':
            self.link = Tinyurl.tinyurl_short(self.url)
        elif self.provider == "bitly":
            self.link = Bitly.bitlyurl_short(self.url)
        return self.link
