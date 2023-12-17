from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MeRoot1234.+',
    'database': 'dbproj',
}

# Create a connection to MySQL
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

@app.route('/')
def index():
    query = "SELECT * FROM co2_production"
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Columns names
    columns = [i[0] for i in cursor.description]

    return render_template('index.html', columns=columns, results=results)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        # Insert user into the database
        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, email))
        conn.commit()

        return f'User {username} added successfully!'

    return render_template('add_user.html')  # Create an HTML form to add users

if __name__ == '__main__':
    app.run(debug=True)