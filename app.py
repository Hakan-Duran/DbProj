from flask import Flask, render_template, request, send_file, redirect
import mysql.connector
import os
import plotly.express as px
import pandas as pd
from insert import insert
from delete import delete
from update import update

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MeRoot1234.+',
    'database': 'archive',
}

# Create a connection to MySQL
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

def get_data_from_database(table, date):
    if table == "co2_production":
        # Fetch necessary data for map creation
        cursor.execute(f'SELECT Country, co2_prod_{date} FROM {table}')
        result = cursor.fetchall()
        
    if table == "gross_national_income_per_capital":
        cursor.execute(f'SELECT Country, gnipc_{date} FROM {table}')
        result = cursor.fetchall()
        
    if table == "human_development_index":
        cursor.execute(f'SELECT Country, hdi_{date} FROM {table}')
        result = cursor.fetchall()
        
    if table == "life_expectancy_by_birth":
        cursor.execute(f'SELECT Country, le_{date} FROM {table}')
        result = cursor.fetchall()
        
    else:
        print("table is not exist")

    return pd.DataFrame(result, columns=['Country', 'value'])


@app.route('/world_map')
def world_map():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    table = request.args.get('table')
    date = request.args.get('date')
    df = get_data_from_database(table, date)
    cursor.close()
    conn.close()
    

    if df.empty:
        return 'No data available.'

    # Adjust necessary values for map creation
    fig = px.choropleth(df, locations='Country', locationmode='country names', color='value', template='plotly', color_continuous_scale='Viridis')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return render_template('world_map.html', plot=fig.to_html(full_html=False))

@app.route('/world')
def world():
    return render_template('world.html')


@app.route('/project')
def project():
    pdf_directory = os.path.join(os.path.dirname(__file__), 'docs')
    pdf_path = os.path.join(pdf_directory, 'Project.pdf')
    return send_file(pdf_path, as_attachment=False)

@app.route('/edit', methods=['GET', 'POST'])
def edit(table=None):
    if request.method == 'GET':
        return render_template('edit.html', table=table)
    if request.method == 'POST':
        table = request.form['table']
        cud = request.form['cud']
        url = f'/edit/{table}/{cud}'
        return redirect(url)

@app.route('/edit/<table>', methods=['GET', 'POST'])
def edittable(table=None):
    if request.method == 'GET':
        return render_template('edit.html', table=table)
    if request.method == 'POST':
        cud = request.form['cud']
    url = f'/edit/{table}/{cud}'
    return redirect(url)

@app.route('/edit/<table>/insert', methods=['GET', 'POST'])
def insertf(table=None):
    post = None # This variable is for insert.html to show related content
    if request.method == 'GET':
        return render_template('insert.html', table=table, post=post)
    if request.method == 'POST':
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        post = 1
        query = insert(table, request) # SQL query is getting from insert.py
        print(query)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('insert.html', table=table, post=post)

@app.route('/edit/<table>/update', methods=['GET', 'POST'])
def updatef(table=None):
    post = None
    if request.method == 'GET':
        return render_template('update.html', table=table, post=post)
    if request.method == 'POST':
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        post = 1
        query = update(table, request) # SQL query is getting from update.py
        print(query)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('update.html', table=table, post=post)

@app.route('/edit/<table>/delete', methods=['GET', 'POST'])
def deletef(table=None):
    post = None
    if request.method == 'GET':
        return render_template('delete.html', table=table, post=post)
    if request.method == 'POST':
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        post = 1
        query = delete(table, request) # SQL query is getting from delete.py
        print(query)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('delete.html', table=table, post=post)
    
@app.route('/list/<schema>/search', methods=['GET', 'POST'])
@app.route('/list/<schema>/search/<country>')
@app.route('/list/<schema>/search/<country>/<column>/<order>')
def search(schema=None, column=None, order=None, country=None):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    next_order = 'asc'
    query = "SELECT * FROM "
    columns = None
    results = None
    
    if request.method == 'POST':
        country = request.form.get('country')
        url = f'/list/{schema}/search/{country}'
        return redirect(url)
    
    if schema:
        query += f"`{schema}`"
        
    if country:
        query += f" WHERE country LIKE '%{country}%'"
        print(query)
        
    if column and order:
        column = column.strip()
        query += f" ORDER BY `{column}` {'ASC' if order == 'asc' else 'DESC'}"
        next_order = 'desc' if order == 'asc' else 'asc'
    
    if schema:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [i[0] for i in cursor.description]
    
    cursor.close()
    conn.close()

    return render_template('list.html', schema=schema , columns=columns, results=results , sorted_column=column, sorted_order=order, next_order=next_order, country=country)


@app.route('/list')
@app.route('/list/<schema>')
@app.route('/list/<schema>/<column>/<order>')
def list(schema=None, column=None, order=None, country=None):
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
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
    
    cursor.close()
    conn.close()

    return render_template('list.html', schema=schema , columns=columns, results=results , sorted_column=column, sorted_order=order, next_order=next_order, country=country)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
