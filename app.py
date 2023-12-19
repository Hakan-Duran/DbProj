from flask import Flask, render_template, request, send_file
import mysql.connector
import os

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

@app.route('/project')
def project():
    # Assuming the PDF file is in the 'docs' directory relative to the script
    pdf_directory = os.path.join(os.path.dirname(__file__), 'docs')
    pdf_path = os.path.join(pdf_directory, 'Project.pdf')
    return send_file(pdf_path, as_attachment=False)

@app.route('/list')
@app.route('/list/<schema>')
@app.route('/list/<schema>/<column>/<order>')
def list(schema=None, column=None, order=None):
    
    next_order = 'asc'
    query = "SELECT * FROM "
    columns = None
    results = None
    
    if schema:
        query += f"`{schema}`"
        
    if column and order:
        column = column.strip()
        query += f" ORDER BY `{column}` {'ASC' if order == 'asc' else 'DESC'}"
        next_order = 'desc' if order == 'asc' else 'asc'
    
    if schema:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [i[0] for i in cursor.description]

    return render_template('list.html', schema=schema , columns=columns, results=results , sorted_column=column, sorted_order=order, next_order=next_order)

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

if __name__ == '__main__':
    app.run(debug=True)
