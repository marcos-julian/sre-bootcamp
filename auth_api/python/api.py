from flask import Flask
from flask import jsonify
from flask import request
from methods import Token, Restricted

app = Flask(__name__)
login = Token()
protected = Restricted()


# Just a health check
@app.route("/")
def url_root():
    return "OK" 


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    payload = request.get_json()
    username = payload['username']
    password = payload['password']
    encoded_jwt = login.generate_token(username, password)
    if encoded_jwt is None:
        return jsonify({"error": "Incorrect Username or Password",}), 403
    res = {
        "data": encoded_jwt 
    }
    return jsonify(res), 201


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')
    if auth_token is None:
        return jsonify({"error": "missing Authorization header",}), 400
    data = protected.access_data(auth_token)
    if data is None:
        return jsonify({"error": "Invalid token",}), 403
    res = {
        "data": data 
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
