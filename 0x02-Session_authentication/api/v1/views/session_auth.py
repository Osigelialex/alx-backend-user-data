#!/usr/bin/env python3
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """handles session login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({ "error": "email missing" }), 400

    if password is None or password == '':
        return jsonify({ "error": "password missing" }), 400

    found = False
    found_user = None

    users = User.search({'email': email})
    if len(users) == 0:
        return jsonify({ "error": "no user found for this email" }), 404

    for user in users:
        if user.is_valid_password(password):
            found = True
            found_user = user

    if not found:
        return jsonify({ "error": "wrong password" }), 401

    from api.v1.app import auth

    session_id = auth.create_session(found_user.id)
    response = jsonify(state=0, msg=user.to_json())
    session_name = os.getenv('SESSION_NAME', None)
    response.set_cookie(session_name, session_id)
    return response
