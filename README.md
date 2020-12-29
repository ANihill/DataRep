# Data Representation and Querying Project
This repository contains the code for the Project for the module Data Representation and Querying. The primary function of this app is to provide the user with an interface to store the details of football players on a team.

# Repository Layout
The repository contains two database access objects, SquadDAO and AuthDAO.
The main Flask application is contained in the file server.py.
The templates folder contains the html files for rendering the Flask application.
initdb.sql contains the sql commands from creating the required tables in this project
requirents.txt contain the venv requirements for the project

### SquadDAO
This contains the logic for connecting to the squad database and performing CRUD operations. It is here the commands for finding players in the database, adding new players, updating player details, and deleting player entries.

### AuthDAO
This contains the logic for users logging into the Flask application. The code contained here has commands for processing the login, registering a new user, and checking whether a username is already in use.

### Server.py
The server.py app contains the routes for the Flask application.
The code from creating the log in system is adapted from [codeshack.io](https://codeshack.io/login-system-python-flask-mysql/).


### Templates 
The code for the home.html file is adapted from the from [BookDAO](https://github.com/andrewbeattycourseware/dataRepresenation2020/blob/master/code/week09-server1linktoDB.py/bookDAO.py) from week 09 of the coursework.
The code for making the player table sortable is from [codepen.io](https://codepen.io/dcode-software/pen/zYGOrzK).

# Running the Application
- Run initdb.sql in mysql to create required database and tables.
- Create dbconfig.py in project directory containing the following code:

```
mysql = {
    'host': "localhost",
    'user': '', # your own username goes here 
    'password': '', # your own password goes here
    'database': 'team'
}
```
- Navigate to project directory from the command line 
- Run the following command python server.py
- Open the Flask application on localhost.

# Using the Application
- You will now be presented with a login page.
- Before logging in an account must be registered.
- Click Register
- Enter username and password and then click register.
- You will be returned to login page where you can now login with username and password you have created.
- Once logged in you can create a new entry into the database by clicking 'create' or you can logout by clicking 'logout'.
- When creating a new player you choose a number, name, position, and age.
- Clicking create will bring you back to player table where you will see the new entry.
- Entries can be updated by clicking 'update' or deleted by clicking 'delete' beside each entry.
- Updating and entry allows you to change the name, position, or age of a player.
