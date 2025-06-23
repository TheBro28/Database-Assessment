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




position = input('What position players do you want to see: ')

print_parameter_query("firstname, surname, appearances, awards, rating, clean_sheets, goals_conceded, wins, losses", "position = ? ORDER BY rating DESC",position)

menu_choice =""
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Liverpool Football Club player statistics database\n\n'
                        'Type the letter for the information you want to see:\n'
                        'A - Defender Player Statistics\n'
                        'B - English Players\n'
                        'C - Midfielders and Striker Player Statistics\n'
                        'D - Players with more than 1 Goal\n'
                        'E - Top 10 Players with the most Passes\n' 
                        'F - Top 5 Players with the most Goals Scored\n'
                        'Z - Exit\n\n'
                        'Type option here: ')
    menu_choice = menu_choice.upper()
