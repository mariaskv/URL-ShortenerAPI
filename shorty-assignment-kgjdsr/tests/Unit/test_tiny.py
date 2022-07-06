from shorty.providers.tinyurl.tiny_url import *

# Check that the programm works correctly with tinyurl shortener

def test_tiny():
    output = Tinyurl.tinyurl_short("https://www.youtube.com/?hl=EL")
    assert output.startswith("https://tinyurl.com/")