I did not successfully implement the idea I pitched in the previous sprint.  The idea was to create a forum-like application that would allow people to post and respond to other posts.  I have very little experience with Python and, upon doing some research, realized that was a much larger task than I had originally expected.  My research included html templates, linking php with python to add pages, and also including css.  I ended up creating a simple page with minor css styling and some embedded html that gives information about me.  Ideally, I want to improve this page so others can have customized information.

Below are a couple of the links I visited and read.  Though there were more that I didn't list.

https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask - Collecting/utilizing form data

https://medium.com/@mahmudahsan/how-to-run-javascript-in-python-web-scraping-web-testing-16bd04894360 - For incorporating JavaScript for form submission.

https://realpython.com/python-web-applications/ - General article about web apps using Python.



Setup has not changed from this.
# google-client-app
Flask, Flask-Login, Login with Google, App setup as Google Client

Installation with Pipenv:

```
pipenv install
```

Installation without Pipenv:

```
pip install -r requirements.txt
```

Initalize the database by running app.py for the first time:

```
python app.py
```

Should see "Initialized the database."

Run the command again to start the Flask web server locally:

```
python app.py
```
