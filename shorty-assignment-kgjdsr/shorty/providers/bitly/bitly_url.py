import requests
import json

# Class Bitly is responsible for shortening a url using bitly

class Bitly:
    def bitlyurl_short(url):

        header = {'Authorization':'4a410e924ad26bf27281e7a46ea128028ce46404', 'Content-Type':'application/json'}

        groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=header)

        if groups_res.status_code == 200:
            groups_data = groups_res.json()['groups'][0]
            guid = groups_data['guid']
        else:
            print("Cannot get GUID")

        data = {
            "long_url": url,
            "group_guid": guid
        }

        short_link_resp = requests.post('https://api-ssl.bitly.com/v4/shorten',json=data, headers=header)

        if short_link_resp.status_code != 200:
            return "ERROR"

        short_link_json = short_link_resp.json()
        short_link = short_link_json["link"]
        return short_link
