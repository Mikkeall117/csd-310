""" 
    Title: pysports_queries.py
    Author: Michael McNulty
    Date: February 14 2021
    Description: This program
"""

# this imports the mysql.connector to the program. 
import mysql.connector
from mysql.connector import errorcode

# this creates a list of connection configuration information to be 
# used later in this program. 
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# tries to connect to the database using the config information above.
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    # runs the SELECT query from the team table.
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # gets the results from the SELECT query above.
    teams = cursor.fetchall()

    print("\n-- DISPLAYING TEAM RECORDS --")

    # iterates through all the teams information and displays the results for each record.
    for team in teams: 
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    # runs the SELECT query from the player table.
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # gets the results from the SELECT query above.
    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")

    # iterates through all the teams information and displays the results for each record.
    for player in players: 
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\nPress any key to continue... ")

# if the ER_ACCESS_DENIED_ERROR or ER_BAD_DB_ERROR errors are presented
# this prints the appropriate error message based on the error. 
except mysql.connector.Error as err:
    if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
# this ensures the connection to the database closes correctly 
# and does not cause any issues from not being closed securely.
finally:
    db.close()
