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
        print(f"{params}")
        for param in params:
            print(f"{param}, ")
            db[param[0]] = param[1]

    else:
        raise Exception('Section {0] not found in the {1} file'.format(section,filename))

    print(f"{db}")
    return db


def connect():
    #connect to the postgres database server
    conn = None

    try:
        #read connection parameters
        params = config('config.ini','Database')
        print(f'Connecting to Postgres Database  ')
        conn = psycopg2.connect(host="localhost",database="Suppliers",user="postgres",password="Admin@123")

        #create a cursor
        cur = conn.cursor()
        print(cur)

        cur.execute('select * from customer')
        result = cur.fetchall()
        print(result)
        for i in result:
            print(i)

        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')



if __name__ == '__main__':
    connect()









