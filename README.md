# SQLAlchemy exercise is to perform a climate analysis about Hawaii.   
Part 1: Analyze and Explore Hawaii Climate Data
Part 2: Design a Climate App
Tools: SQLAlchemy, Python, Pandas, Matplotlib

# Part 1: Analyze and Explore the Climate Data
Steps:
1. Use Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. 
2. Source files: climate_starter.ipynb and hawaii.sqlite
3. Use the SQLAlchemy create_engine() function to connect to the SQLite database: engine = create_engine("sqlite:///Resources/hawaii.sqlite")
4. Use the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement.
5. Link Python to the database by creating a SQLAlchemy session.
7. Perform a precipitation analysis.
8. Perform a station analysis.

## Precipitation Analysis
1. Find the most recent date in the dataset.
- most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
- print(most_recent_date)
- The most recent date is:  2017-08-23
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.  Note, only the "date" and "prcp" values were selected.
- prior_year= dt.date(2017,8,23) - dt.timedelta(days=365)
- results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prior_year).all()
3. Load the query results into a Pandas DataFrame. Explicitly set the column names.
- prior_year_precipitation_df = pd.DataFrame(results, columns=("date","precipitation"))
5. Sort the DataFrame values by "date".
- date_sorted_df = prior_year_precipitation_df.sort_values('date')
6. Plot the results by using the DataFrame plot method
- date_sorted_df.plot(x='date',y='precipitation',rot=90)
- plt.xlabel('Date')
- plt.ylabel('Precipitation (Inches)')
- plt.legend(loc='upper right')
- plt.xticks(rotation=45)
- plt.show()
![image](https://github.com/CMccormick0003/sqlalchemy-challenge/assets/120672518/627e5d09-ce77-4f39-b1c1-25db90e2e4ef)
7. Use Pandas to print the summary statistics for the precipitation data.
- date_sorted_df.describe()

![image](https://github.com/CMccormick0003/sqlalchemy-challenge/assets/120672518/f742396b-f972-4af4-93fb-490dc033db94)

## Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
- station_count = session.query(Measurement.station).distinct().count()
- print(station_count)
### The total number of stations: 9

2. Design a query to find the most-active stations (that is, the stations that have the most rows). List the stations and observation counts in descending order.
- session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
![image](https://github.com/CMccormick0003/sqlalchemy-challenge/assets/120672518/9a538282-44ba-415e-8fab-3eaf122daa32)

3. ### Which station id has the greatest number of observations?
- most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()
- print("The most active station is:", most_active_station[0])
### The most active station is: USC00519281

4. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- temperature_stats = session.query(func.min(Measurement.tobs).label('lowest_temperature'),
                                  func.max(Measurement.tobs).label('highest_temperature'),
                                  func.avg(Measurement.tobs).label('average_temperature')).\
        filter(Measurement.station == 'USC00519281').all()

- lowest_temp = temperature_stats[0].lowest_temperature
- highest_temp = temperature_stats[0].highest_temperature
- avg_temp = temperature_stats[0].average_temperature

- print("Lowest Temperature:", lowest_temp)
- print("Highest Temperature:", highest_temp)
- print("Average Temperature:", avg_temp)

![image](https://github.com/CMccormick0003/sqlalchemy-challenge/assets/120672518/c5aeaba9-e346-4053-bc33-1e868bd7d673)

5. Design a query to get the previous 12 months of temperature observation (TOBS) data. Filter by the station that has the greatest number of observations. Query the previous 12 months of TOBS data for that station.
- from pandas.plotting import table
- prior_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
- results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prior_year).all()
    
6. Plot the results as a histogram with bins=12
- df= pd.DataFrame(results, columns = ['tobs'])
- df.plot.hist(bins = 12)
- plt.tight_layout()
- plt.xlabel("Temperature (F)")
- plt.ylabel("Frequency (# Days)")

![image](https://github.com/CMccormick0003/sqlalchemy-challenge/assets/120672518/e819bf56-da26-4d91-a12a-5d075fd7fd71)

7. Close your session.

# Part 2: Design Your Climate App
Now that we have completed out initial analysis, let's design a Flask API based on the queries that were just developed. 
1. Use Flask to create your routes 
2. Start at the homepage.
3. List all the available routes.
- /api/v1.0/precipitation
4. Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
5. Return the JSON representation of the dictionary.
- /api/v1.0/stations
6. Return a JSON list of stations from the dataset.
- /api/v1.0/tobs
7. Query the dates and temperature observations of the most-active station for the previous year of data.
8. Return a JSON list of temperature observations for the previous year.
- /api/v1.0/<start> and /api/v1.0/<start>/<end>
9. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
10. For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
11. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.  Note, join the station and measurement tables for some of the queries.
12. Use the Flask jsonify function to convert the API data to a valid JSON response object.
