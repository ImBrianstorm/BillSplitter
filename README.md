# BillSplitter

Split your bills with your friends with this awesome website [SOON]

## Local Installation

If you want to run a local server to test, you need the following:

* [**Python 3.5**](https://www.python.org/downloads/ "Install Python")
* [PIP](https://www.makeuseof.com/tag/install-pip-for-python/ "Install PIP")
* [virtualenv](https://virtualenv.pypa.io/en/latest/installation/ "Install virtualenv")

Then, you can type this in your terminal to activate your virtual environment:

```bash
cd BillSplitter/
virtualenv -p python3 venv
source venv/bin/activate
```
You must do `source venv/bin/activate` every time you want to start your virtual environment.
And if you want to deactive it, just type it like this: `deactivate`

Now, we can proceed to install Django and the remaining dependencies:

```bash
pip install -r requirements.txt
```

Now, we can prepare Django, so we can run it:

```bash
python manage.py makemigrations
python manage.py migrate
```

It's done! You can run it on your computer with a local server:

```bash
python manage.py runserver
```

The previous command will run a local server on http://localhost:8000, so you can enter with your favorite browser and enjoy it!

If you want to use another host or another port, you can make it like this:

```bash
#To use another port, in the example, 8080
python manage.py runserver 8000

#And also, you can use another host, like 0.0.0.0, like this
python manage.py runserver 0.0.0.0:8000
```
Consider that you can't use any port you want, [here is a port list](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) if you want to check it

To shutdown the server, type `Control-C` on your computer over the server terminal.

> With love, [@imbrianstorm](https://twitter.com/ImBrianstorm "Follow me on Twitter")
