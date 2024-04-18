#!/usr/bin/python3
"""
Starting Flask WEB application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


# Creating an instance of Flask class
app = Flask('__name__', template_folder="web_flask/templates")

@app.route("/cities_by_states", strict_slashes=False)
def state_city():
    #states = storage.all(State).values()
    cities =  storage.all(City).values()
    return render_template("8-cities_by_states.py", cities=cities)

@app.teardown_appcontext
def storage_close(exception):
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')