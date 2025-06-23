# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Music_Lessons.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Music_Lessons.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()



# Import the libraries to connect to the database and present the information in tables

import sqlite3

from tabulate import tabulate


# This is the filename of the database to be used

DB_NAME = 'Liverpool_FC.db'

# This is the SQL to connect to all the tables in the database

TABLES = (" liverpool_fc "

           "LEFT JOIN positions ON liverpool_fc.position_id = positions.position_id " )

def print_parameter_query(fields:str, where:str, parameter):

    """ Prints the results for a parameter query in tabular form. """

    db = sqlite3.connect(DB_NAME)

    cursor = db.cursor()

    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)

    cursor.execute(sql,(parameter,))

    results = cursor.fetchall()

    print(tabulate(results,fields.split(",")))

    db.close()  



menu_choice =""
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Liverpool Football Club player statistics database\n\n'
                        'Type the letter for the information you want to see:\n'
                        'A - Statistics based on player positions\n'
                        'B - English Players\n'
                        'C - Players with more than 1 Goal\n'
                        'D - Top 10 Players with the most Passes\n'
                        'E - Top 5 Players with the most Goals Scored\n' 
                        'F - Players who have been with Liverpool for the longest to shortest time\n'
                        'Z - Exit\n\n'
                        'Type option here: ')
    menu_choice = menu_choice.upper()

    
    if menu_choice == 'A':
        while True:
            position = input('What position players do you want to see? (Goalkeeper, Defender, Midfielder, Forward): ').title()
            if position in ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']:
                print_parameter_query("firstname, surname, appearances, player_number, clean_sheets, saves, goals_conceded, goals_scored, assists, wins, losses, market_value, contract_signed", "position = ? ORDER BY rating DESC",position)
                break
            else:
                print("Invalid position. Please enter in one of the following: Goalkeeper, Defender, Midfielder, Forward.")
    elif menu_choice == 'B':
        print_query ("English Players")
    elif menu_choice == 'C':
        print_query ("Player with more than 1 goal scored")
    elif menu_choice == 'D':
        print_query ("Top 10 highest passes")
    elif menu_choice == 'E':
        print_query ("Top 5 goal scoring players")
    elif menu_choice == 'F':
        print_query ("Liverpool Veterans")
    elif menu_choice == 'Z':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
