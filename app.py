from flask import Flask, request

app = Flask(__name__)

@app.route('/ua')
def welcome():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Welcome to 2024!</h1><br>User Agent: {user_agent}'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

