# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import psycopg2
from configparser import ConfigParser

def config(filename='config.ini', section='Database'):
    #create a parser
    parser = ConfigParser()
    #read config file
    parser.read(filename)

    #get section, defaults to Database
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = params[1]
    else:
        raise Exception('Section {0] not found in the {1} file'.format(section,filename))

    return db


def connect():
    #connect to the postgres database server
    conn = None

    try:
        #read connection parameters
        params = config('config.ini','Database')
        print(f'Connecting to Postgres Database {params[1]} ')
        conn = psycopg2.connect(**params)

        #create a cursor
        cur = conn.cursor()

        cur.execute('select * from customer')
        print(cur)
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')











