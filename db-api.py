import errno
from flask import request, redirect
from flask import Flask
import sqlite3
import os

app = Flask(__name__)

# check if database exists, if not create db
if not os.path.isfile('database.db'):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE messages (id INTEGER PRIMARY KEY, content TEXT, ip TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    #return all messages
    c = conn.cursor()
    c.execute('''SELECT * FROM messages''')
    messages = c.fetchall()
    conn.close()
    return str(messages)

@app.route('/msg', methods=['POST'])
def msg():
    try:
        #add message to database along with request ip    
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''INSERT INTO messages (content, ip) VALUES (?, ?)''', (request.form.get('message'), request.remote_addr ))
        conn.commit()
        conn.close()
        return redirect('localhost:5173')
    except Exception as e:
        print(e)
        return redirect('localhost:5173')
    
if __name__ == '__main__':
    app.run(debug=True)