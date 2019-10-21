from time import time
import pyodbc 
import pandas as pd

### PARAMETERS ###
# Set these parameters in order to use this script
server_name = 'YOUR_SERVER_NAME'
db_name  = 'YOUR_DB_NAME'
username = 'USERNAME'
password = 'PASSWORD'


def retrieve_table_from_db(table):
    '''
    Args:
        table (str): Name of the table to retrieve from DB
    Returns:
        (pandas.DataFrame)
    '''
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'+
        'SERVER='+server_name+
        ';DATABASE='+db_name+
        ';UID='+username+
        ';PWD='+ password
    )
    cursor = cnxn.cursor()
    # Helper func
    def select_all_from(table, verbose=False):
        t0 = time()
        q = 'SELECT * FROM ' + table
        if verbose: print(str(table), ' loaded in ', str(time()- t0), 's')
        return pd.read_sql(q,cnxn)

    t0 = time()
    df = select_all_from('TABLE_NAME', verbose=True)
    print('table loaded')
    return df