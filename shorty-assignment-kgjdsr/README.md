Mission
-------

Your mission, should you choose to accept it, is to build a microservice called `shorty`, 
which supports two URL shortening providers: [bit.ly](https://dev.bitly.com/) and [tinyurl.com](https://gist.github.com/MikeRogers0/2907534).
You don't need to actually sign up to these providers, just integrate with their API. The
service exposes a single endpoint: `POST /shortlinks`. The endpoint should receive
JSON with the following schema:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The URL to shorten                 |
| provider | string | N        | The provider to use for shortening |

The response should be a `Shortlink` resource containing:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The original URL                   |
| link     | string | Y        | The shortened link                 |

For example:
```json
{
    "url": "https://example.com",
    "link": "https://bit.ly/8h1bka"
}
```

You are free to decide how to pick between the providers if one is not requested and what
your fallback strategy is in case your primary choice fails. Your endpoint needs to return
a JSON response with a sensible HTTP status in case of errors or failures.

What you need to do
-------------------

1. Create a Python env (using Python 3.6+) and install the requirements.
2. Build the `POST /shortlinks` endpoint. We've provided a skeleton API using `flask`.
3. Write some tests. We've provided a test blueprint using `pytest`.

Deliverable
-----------

You should deliver your solution as a Pull Request in your repo. Document your design choices and anything else you think we need to know in the PR description.

What we look for
----------------

In a nutshell, we're looking for tidy, production-quality code, a scalable design and sensible
tests (unit tests, integration tests or both?). Imagine that your code will be read by other 
developers in your team – keep them happy :-)

Resources
---------

1. `Flask`: http://flask.pocoo.org/
2. `pytest`: http://pytest.org/latest/
3. `virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/latest/
4. `HTTP statuses`: https://httpstatuses.com/


----------------------

Documentation

Execution: To execute the programm simply run $ bash ./env.sh inside the root directory. This way you run the server using python virtual environment. 
The server is now running under localhost(probably http://localhost:5000/). 

After the server is running a simple html page is displayed under the localhost. This page includes a simple html form in order to submit your json formed request.
After pressing the Submit Button your result or your error message will be displayed.

The basic structure of the project is as follows:

shorty:
    providers:
        bitly:
            bitly_url.py
        tinyurl:
            tinyurl.py
        provider.py
    templates:
        index.html
    tests:
        Unit:
            test_bitly.py
            test_tiny.py
            test_provider.py
        OtherTests:
            user_cases.py
        conftest.py

What I did: I implemented both POST/shortlinks and GET/shortlinks endpoints in the API. Only the POST does the work it has to be but GET is there to inform the user to use the POST.
I also implemented the classes of the providers(bitly/tiny) that are responsible for shortening the url. I also created some tests both unit and functional to verify the correctnes
of the programm.

Tests: You can run the tests as follow:

Unit tests: Inside the tests directory run $ pytest -v Unit/
Other tests: Inside the tests directory run $ pytest -v OtherTests/

DISCLAIMER: The OtherTests are currently NOT working due to some problem with the installed python version in my system. Although you can still check them and get an idea of how they should 
be implemented.

There are more info in the comments of my code.

