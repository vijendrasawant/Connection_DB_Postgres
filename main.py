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










