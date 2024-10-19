from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)


db_config = {
    'user': 'root',
    'password': '1903',
    'host': 'localhost',
    'database': 'spotify_db'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-query', methods=['POST'])
def run_query():
    query_id = request.json.get('query_id')
    param = request.json.get('param')  # Get the parameter from the request body
    conn = get_db_connection()
    cursor = conn.cursor()

    from queries import queries
    query = queries.get(query_id)

    if query:
        if query_id == 1 and param:  # Only pass the parameter for Query 1
            cursor.execute(query, (f"%{param}%",))  # Pass the parameter as a tuple
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        conn.close()
        return jsonify(result)
    else:
        return jsonify({'error': 'Query not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
