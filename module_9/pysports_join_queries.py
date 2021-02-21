""" 
    Title: pysports_join_queries.py
    Author: Michael McNulty
    Date: February 21 2021
    Description: This program creates an inner join connecting the player and team tables by team_id and prints the results.
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

    # creates the inner join between the two tables.
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    # gets the results from above.
    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")

    # goes through each entry from the cursor and prints it along with it's correct label.
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0],player[1],player[2],player[3]))

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
