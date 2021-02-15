""" 
    Title: mysql_test.py
    Author: Michael McNulty
    Date: February 14 2021
    Description: This program tests to see if it's able to access two different tables in the pysports database.
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

    # if the program is able to connect to the database successfully, 
    # this message is printed with the appropriate values from the config
    # information above.
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

# if the ER_ACCESS_DENIED_ERROR or ER_BAD_DB_ERROR errors are presented
# this prints the appropriate error message based on the error. 
except mysql.connector.Error as err:
    if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)
# this ensures the connection to the database closes correctly 
# and does not cause any issues from not being closed securely.
finally:
    db.close()

