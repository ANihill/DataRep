from flask import Flask, url_for, request, redirect, abort, jsonify, session, render_template
from SquadDAO import squadDAO
from AuthDAO import authDAO
import re

app = Flask(__name__, static_url_path='', static_folder='static')

app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'




@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = authDAO.login(username, password)
        if account:
            session['loggedin'] = True
            session['username'] = username
            return redirect(url_for('home'))

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)


@app.route('/login/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        account = authDAO.checkUser(username)
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password:
            msg = 'Please fill out the form!'
        else:
            authDAO.register(username, password)
            authDAO.login(username, password)
            session['loggedin'] = True
            return redirect(url_for('home'))

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@app.route('/login/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))



@app.route('/squad')
def getAll():
    return jsonify(squadDAO.getAll())


@app.route('/squad/<int:playerNumber>')
def findById(playerNumber):
    return jsonify(squadDAO.findById(playerNumber))




@app.route('/squad', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    player = {
        "playerNumber": request.json["playerNumber"],
        "playerName": request.json["playerName"],
        "position": request.json["position"],
        "age": request.json["age"]
    }
    return jsonify(squadDAO.create(player))



@app.route('/squad/<int:playerNumber>', methods=['PUT'])
def update(playerNumber):
    foundPlayer = squadDAO.findById(playerNumber)
    print(foundPlayer)
    if foundPlayer == {}:
        return jsonify({}), 404
    currentPlayer = foundPlayer
    if 'playerName' in request.json:
        currentPlayer['playerName'] = request.json['playerName']
    if 'position' in request.json:
        currentPlayer['position'] = request.json['position']
    if 'age' in request.json:
        currentPlayer['age'] = request.json['age']
    squadDAO.update(currentPlayer)

    return jsonify(currentPlayer)




@app.route('/squad/<int:playerNumber>', methods=['DELETE'])
def delete(playerNumber):
    squadDAO.delete(playerNumber)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)
