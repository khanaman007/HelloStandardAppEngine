import flask

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


@app.get("/")
def hello():
    """Return a friendly HTTP greeting.............."""
    return "Hello From Standard App Engine! with cron job and stop version\n"



if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="0.0.0.0", port=8080, debug=True)