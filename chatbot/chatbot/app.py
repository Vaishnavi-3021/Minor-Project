from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define database connection parameters
host = "localhost"
user = "root"
password = "password"
database = "my_database"

# Connect to the database
db = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Define a cursor object to interact with the database
cursor = db.cursor()

# Define a route to display data from a table
@app.route('/')
def display_data():
    # Define a query to fetch data from a table
    query = "SELECT * FROM my_table"

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Render the results on a web page
    return render_template('data.html', results=results)

# Close the database connection
db.close()

if __name__ == '__main__':
    app.run(debug=True)
import mysql.connector

# Define database connection parameters
host = "localhost"
user = "root"
password = "password"
database = "my_database"

# Connect to the database
db = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Define a cursor object to interact with the database
cursor = db.cursor()

# Define a query to fetch data from a table
query = "SELECT * FROM my_table"

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the database connection
db.close()


