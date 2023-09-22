# Flask section

This section is about Flask, a Python framework.

## Files

- [0-hello_route.py](0-hello_route.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!".

- [1-hbnb_route.py](1-hbnb_route.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!", route `/hbnb` displays "HBNB".

- [2-c_route.py](2-c_route.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!", route `/hbnb` displays "HBNB", route `/c/<text>` displays "C" followed by the value of the `text` variable (replace underscore _ symbols with a space).

- [3-python_route.py](3-python_route.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!", route `/hbnb` displays "HBNB", route `/c/<text>` displays "C" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/python/(<text>)` displays "Python" followed by the value of the `text` variable (replace underscore _ symbols with a space).

- [4-number_route.py](4-number_route.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!", route `/hbnb` displays "HBNB", route `/c/<text>` displays "C" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/python/(<text>)` displays "Python" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/number/<n>` displays "`n` is a number" only if `n` is an integer.

- [5-number_template.py](5-number_template.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!", route `/hbnb` displays "HBNB", route `/c/<text>` displays "C" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/python/(<text>)` displays "Python" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/number/<n>` displays "`n` is a number" only if `n` is an integer, route `/number_template/<n>` displays a HTML page only if `n` is an integer.

- [6-number_odd_or_even.py](6-number_odd_or_even.py) - Script that starts a Flask web application listening on 0.0.0.0, port 5000. Route `/` displays "Hello HBNB!", route `/hbnb` displays "HBNB", route `/c/<text>` displays "C" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/python/(<text>)` displays "Python" followed by the value of the `text` variable (replace underscore _ symbols with a space), route `/number/<n>` displays "`n` is a number" only if `n` is an integer, route `/number_template/<n>` displays a HTML page only if `n` is an integer, route `/number_odd_or_even/<n>` displays a HTML page only if `n` is an integer.