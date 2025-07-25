from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

# Landing Page
@app.route('/')
def hello_world():
    return 'Hello World'

# Hello Pages
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!'

@app.route('/hello')
def request_name():
    name = request.args.get('name', 'Guest')
    return f'Hello {name}!'

# Log-in page
@app.route('/authenticate', methods=['GET', 'POST'])
def submit_html():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        ip = request.remote_addr
        today = datetime.now()
        today = today.strftime("%Y-%m-%d %H:%M:%S")
        
        if username.strip() == '':
            return "<h1>Invalid username</h1>"
        if password.strip() == '':
            return "<h1>Invalid password</h1>"
        
        log_entry = {
            "timestamp": today,
            "ip": ip,
            "username": username,
            "password": password,
            "path": "/authenticate",
            "method": "POST"
        }
        with open("normal_training.log", "a") as fo:
            fo.write(json.dumps(log_entry) + "\n")
        return render_template('form.html')
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)

