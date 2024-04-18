#!/usr/bin/python3
"""
Starting Flask WEB application
"""

from flask import Flask, render_template
from models import storage
from models.state import State


# Creating an instance of Flask class
app = Flask('__name__', template_folder="web_flask/templates")

@app.route("/cities_by_states", strict_slashes=False)
def state_city():
    states = storage.all(State).values()
    return render_template("8-cities_by_states.py", states=states)

@app.teardown_appcontext
def storage_close(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)