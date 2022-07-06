from sre_constants import SUCCESS
from urllib import response, request
from shorty.providers.provider import Provider
import pytest
import flask
import requests
from shorty import api
# from app.models import post


ERROR_CODE = 400
SUCCESS_CODE = 200

class TestAPI:

    # First test is about to ckeck programm;s behaviour for correct input 
    def test1(self, post):
        output = post(
            '/shortlinks',
            data = {
                "url": "https://www.youtube.com/?hl=EL",
                "provider": "bitly"
            }
        )
        assert response.status_code == SUCCESS_CODE
        assert response.get_json()['url'] is not None

    # This test tests for wrong url and correct provider
    def test2(self, post):
        output = post(
            '/shortlinks',
            data = {
                "url": "htt://www.youtube.com/?hl=EL",
                "provider": "bitly"
            }
        )
        assert response.status_code == ERROR_CODE

    # This test checks for random url and correct provider
    def test3(self, post):
        output = post(
            '/shortlinks',
            data = {
                "url": "aaaa",
                "provider": "bitly"
            }
        )
        assert response.status_code == ERROR_CODE

    # This test checks for no url and correct provider
    def test4(self, post):
        output = post(
            '/shortlinks',
            data = {
                "url": "",
                "provider": "bitly"
            }
        )
        assert response.status_code == ERROR_CODE

    # This test checks for correct url and random provider
    def test5(self, post):
        output = post(
            url = '/shortlinks/',
            data = {
                "url": "https://www.youtube.com/?hl=EL",
                "provider": "bitlaaaay"
            }
        )
        print(response.status_code)
        assert response.status_code == ERROR_CODE

    # This test checks for empty input
    def test6(self, post):
        output = post(
            '/shortlinks',
            data = { }
        )
        assert response.status_code == ERROR_CODE


