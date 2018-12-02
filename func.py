import pyodbc
import pandas as pd
import os.path

def crearConexion(path, pwd):
    """ Create a conection to the database

    Keywords arguments:
    path -> path of the database(mdb)
    pwd -> Password of the database.

    Return:
    conn -> connection to the database
    cursor
    """
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=' + path + ';PWD=' + pwd)
    cursor = conn.cursor()

    return conn, cursor

def saveCSV(df, file):
    """ Create or modify a csv

    Keywords arguments:
    df -> Dataframe we want to save
    file -> File path we want to create or modify
    """
    df.to_csv(file, sep=';', index=False)

    return 'File saved succefully!'

    

def createDF(path, table, *args):
    """ Create a dataframe given the followiong parameters

    Keywords arguments:
    table -> Choose a table from where you want to extract the information
    *args -> Choose the list of columns of the table which you want to extact

    Return:
    df -> Dataframe with the information we are looking for
    """
    df = pd.DataFrame(columns=args)

    diccionario = dict()
    query = ''

    for elem in args:
        query += str(elem)+', ' 
    
    conn, cursor = crearConexion(str(path),'ad4600')
    cursor.execute('SELECT '+ query[0:len(query)-2] +' FROM ' + table)
        
    for row in cursor.fetchall():
        count = 0
        for elem in args:
            diccionario[elem] = row[count]
            count += 1
        df = df.append(diccionario, ignore_index=True)

    conn.close()
        
    return df
