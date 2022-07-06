from urllib import response
import requests

# Class TinyUrl is responsible for shortening a url using tinyurl

class Tinyurl:

    def tinyurl_short(url):
        response = requests.get("https://tinyurl.com/api-create.php", dict(url = url), timeout = 11)

        if response.status_code != 200:
            return "ERROR"
        
        return response.content.decode()