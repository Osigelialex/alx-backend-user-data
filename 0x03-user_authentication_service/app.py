#!/usr/bin/env python3
"""flask app module
"""
from flask import Flask, jsonify, request, make_response, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def index() -> str:
    """index route method
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users() -> str:
    """endpoint for registering users
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        resp = {"email": email, "message": "user created"}
        return jsonify(resp)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """endpoint for logging in users
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        payload = {"email": email, "message": "logged in"}
        resp = make_response(payload)
        resp.set_cookie('session_id', session_id)
        return resp
    else:
        abort(401)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
