from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'dbproj',
}

# Create a connection to MySQL
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

@app.route('/')
@app.route('/<column>/<order>')
def index(column=None, order=None):
    query = "SELECT * FROM co2_production"
    next_order = 'asc'

    if column and order:
        query += f" ORDER BY `{column}` {'ASC' if order == 'asc' else 'DESC'}"
        next_order = 'desc' if order == 'asc' else 'asc'

    cursor.execute(query)
    results = cursor.fetchall()
    columns = [i[0] for i in cursor.description]

    return render_template('index.html', columns=columns, results=results, sorted_column=column, sorted_order=order, next_order=next_order)

@app.route('/search')
def search():
    country = request.args.get('country')

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if country:
        query = "SELECT * FROM co2_production WHERE country LIKE %s"
        cursor.execute(query, (f"%{country}%",))
    else:
        query = "SELECT * FROM co2_production"
        cursor.execute(query)

    results = cursor.fetchall()
    columns = [i[0] for i in cursor.description]

    cursor.close()
    conn.close()

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

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
