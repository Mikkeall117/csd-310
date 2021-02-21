""" 
    Title: pysports_update_and_delete.py
    Author: Michael McNulty
    Date: February 21 2021
    Description: This program inserts records into the player table for Team Galdalf, uses an inner join to view the changes, 
    then changes the newly inserted record to a new team_id, then creates an inner join and prints the new data, then deletes the updated record and creates an inner join again and returns the final output.
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
# this method allows me to create an inner join and print all players to screen multiple times from one set of code.
def showPlayerInfo(cursor, title):
    # creates the inner join between the two tables.
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    # gets the results from above.
    players = cursor.fetchall()

    # prints the correct section label based on the info passed to the method from the title variable.
    print("\n-- {} --".format(title))

    # goes through each entry from the cursor and prints it along with it's correct label.
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0],player[1],player[2],player[3]))

# tries to connect to the database using the config information above.
try:
    # this connects to the pysports database using the config information from above.
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    # this entry will insert the new player information.
    addNewPlayer = ("INSERT INTO player(first_name, last_name, team_id)"
        "VALUES('Smeagol', 'Shire Folk', 1)")

    # this executes the INSERT INTO statement above using the player data above.
    cursor.execute(addNewPlayer)

    # this commits the inserted info to the database.
    db.commit()

    # this will run the showPlayerInfo() method with the correct parameters passed to it.
    showPlayerInfo(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # this will update the information on the newly created user above.
    updatePlayer = ("UPDATE player set team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # this will execute the UPDATE statement above.
    cursor.execute(updatePlayer)

    # this commits the updated info to the database.
    db.commit()

    # this calls the showPlayerInfo() method with the new parameters being passed to it.
    showPlayerInfo(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # this will delete the recently updated player entry.
    deletePlayer = ("DELETE FROM player WHERE first_name = 'Gollum'")

    # this executes the deletePlayer process created above.
    cursor.execute(deletePlayer)
    
    # this commits the deleted info to the database.
    db.commit()

    # calls the showPlayerInfo method with new parameters being passed to the method.
    showPlayerInfo(cursor, "DISPLAYING PLAYERS AFTER DELETE")

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
