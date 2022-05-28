from flask import Flask, render_template, redirect, request, url_for
import requests
import json

app = Flask(__name__)


# The Username & Password of the currently logged-in User
username = None
password = None

session_data = dict()

def save_to_session(key, value):
    """
    @brief Save a key, value pair to the global session object.
    """
    session_data[key] = value

def load_from_session(key):
    """
    @brief load (and pop) the value associated with the given key from the global session object.
    """
    return session_data.pop(key) if key in session_data else None  # Pop to ensure that it is only used once

@app.route("/")
def main_page():
    return render_template('main.html', username=username, password=password)

@app.route("/catalogue")
def catalogue():
    # ================================
    # FEATURE 4 (catalogue)
    #
    # fetch a list of movies from the microservice
    # microservice returns a (python) list of movie strings
    # ================================

    url = "http://movie:5000/api/getMovies"
    response = requests.request("GET", url)
    movies = response.json()["movies"]
    return render_template('catalogue.html', username=username, password=password, movies=movies)

@app.route("/login")
def login_page():

    success = load_from_session('success')
    return render_template('login.html', username=username, password=password, success=success)

@app.route("/login", methods=['POST'])
def actual_login():
    req_username, req_password = request.form['username'], request.form['password']

    # ================================
    # FEATURE 1 (login)
    #
    # send the username and password to the microservice
    # microservice returns True if correct combination, False if otherwise.
    # ================================
    success = None
    url = "http://user:5000/api/login"
    payload = json.dumps({
        "username": str(req_username).lower(),
        "password": str(req_password)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        success = True
    else:
        success = False

    save_to_session('success', success)

    if success:
        global username, password
        username = req_username
        password = req_password
    return redirect('/login')


@app.route("/register")
def register_page():
    success = load_from_session('success')
    return render_template('register.html', username=username, password=password, success=success)


@app.route("/register", methods=['POST'])
def actual_register():

    req_username, req_password = request.form['username'], request.form['password']

    # ================================
    # FEATURE 1 (register)
    #
    # send the username and password to the microservice
    # microservice returns True if username is available, False if otherwise.
    # ================================

    success = None
    url = "http://user:5000/api/register"
    payload = json.dumps({
        "username": str(req_username).lower(),
        "password": str(req_password)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        success = True
    else:
        success = False
    save_to_session('success', success)

    if success:
        global username, password

        username = req_username
        password = req_password
        redirect('/login')

    return redirect('/register')


@app.route("/friends")
def friends():
    success = load_from_session('success')
    return render_template('friends.html', username=username, password=password, success=success)

@app.route("/add_friend", methods=['POST'])
def add_friend():
    global username

    friend_username = request.form['username']
    # ==============================
    # FEATURE 2
    #
    # send the username of the current user and the username of the added friend to the microservice
    # microservice returns True if the friend request is successful (the friend exists & is not already friends), False if otherwise
    # ==============================

    success = None
    url = "http://user:5000/api/addFriend"
    payload = json.dumps({
        "username": str(username).lower(),
        "friend_username": str(friend_username).lower()
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        success = True
    else:
        success = False
    save_to_session('success', success)

    return redirect('/friends')


@app.route("/groups")
def groups():

    create_success = load_from_session('create_success')
    add_success = load_from_session('add_success')
    return render_template('groups.html', username=username, password=password, create_success=create_success, add_success=add_success)


@app.route('/create_group', methods=['POST'])
def create_group():
    global username
    # ==============================
    # FEATURE 8
    #
    # send the groupname to the microservice
    # microservice returns True if the group creation is succesful (the group with this name doesn't exist already), False if otherwise
    # ==============================

    groupname = request.form['groupname']

    success = None
    url = "http://group:5000/api/createGroup"
    payload = json.dumps({
        "owner_username": str(username).lower(),
        "group_name": str(groupname).lower()
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        success = True
    else:
        success = False
    save_to_session('create_success', success)

    return redirect('/groups')


@app.route('/add_friend_to_group', methods=['POST'])
def add_friend_to_group():
    global username
    # ==============================
    # FEATURE 9
    #
    # send the groupname, username, friendname to the microservice
    # microservice returns True if the action is succesful (you are friends, the group exists & you are in the group), False if otherwise
    # ==============================
    groupname, friend_username = request.form['groupname'], request.form['friendname']

    success = None
    url = "http://group:5000/api/addFriendToGroup"
    payload = json.dumps({
        "owner_username": str(username).lower(),
        "friend_username": str(friend_username).lower(),
        "group_name": str(groupname).lower()
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        success = True
    else:
        success = False
    save_to_session('add_success', success)
    return redirect('/groups')

@app.route("/logout")
def logout():
    global username, password

    username = None
    password = None
    return redirect('/')
