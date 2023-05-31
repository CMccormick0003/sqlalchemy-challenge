This SQLAlchemy exercise is to perform a climate analysis about Hawaii.  The exercise has 2 parts.  
# Part 1: Analyze and Explore the Climate Data
# Part 2: Design a Climate App

Tools: SQLAlchemy, Python, Pandas, Matplotlib

# Part 1: Analyze and Explore the Climate Data
Steps:
1. Use Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. 
2. Source files: climate_starter.ipynb and hawaii.sqlite
3. Use the SQLAlchemy create_engine() function to connect to the SQLite database.
4. Use the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement.
5. Link Python to the database by creating a SQLAlchemy session.
6. Perform a precipitation analysis.
7. Perform a station analysis.

## Precipitation Analysis
- Find the most recent date in the dataset.
- Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.  Note, only the "date" and "prcp" values were selected.
- Load the query results into a Pandas DataFrame. Explicitly set the column names.
- Sort the DataFrame values by "date".
- Plot the results by using the DataFrame plot method
- Use Pandas to print the summary statistics for the precipitation data.

## Station Analysis
- Design a query to calculate the total number of stations in the dataset.
- Design a query to find the most-active stations (that is, the stations that have the most rows). 
- List the stations and observation counts in descending order.
- ### Which station id has the greatest number of observations?
- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
- Filter by the station that has the greatest number of observations.
- Query the previous 12 months of TOBS data for that station.
- Plot the results as a histogram with bins=12
- Close your session.

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