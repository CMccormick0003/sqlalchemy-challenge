# Import the dependencies.

import numpy as np

import datetime as dt

import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")

def main():
    return (
        f"This is the Hawaii Climate Analysis API.  Surf's Up! <br/>"    
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/end <br/>"
        f"/api/v1.0/start/end"
    )

# Convert query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp (precipitation) as the value.
app.route("/api/v1.0/precipitation")

def precipitation():
    prior_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prior_year).all()
    session.close()

    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)
 
# session = Session(engine)
# This ia a route definition in in Flask to create an endpoint at "/api/v1.0/stations" - this will respond to HTTP GET requests.
app.route("/api/v1.0/stations")

def station():
    session = Session(engine)
    distinct_stations = session.query(Measurement.station).distinct().all()
    session.close()
    stations =list(np.ravel(results))
    return jsonify(stations=stations)
