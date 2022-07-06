from shorty.providers.bitly.bitly_url import *

# Check that the programm works correctly with bitly shortener

def test_bitly():
    output = Bitly.bitlyurl_short("https://www.youtube.com/?hl=EL")
    assert output.startswith("https://bit.ly/")