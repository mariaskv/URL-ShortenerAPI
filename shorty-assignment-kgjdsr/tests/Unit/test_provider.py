import pytest
from shorty.providers.provider import *

# Check that the programm works correctly when giving an url and a provider

def test_provider():
    request = {"url": "https://www.youtube.com/", "provider": "tinyurl"}

    provider = Provider(request)

    output = provider.short()

    # The result must starts with https://tinyurl.com/ as long as it has been shortened with tinyurl
    assert output.startswith("https://tinyurl.com/")