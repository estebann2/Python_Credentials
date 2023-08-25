import pyodbc

def execute_query():
    """
    Run a SQL query
    """

    # Credenciales
    server = 'server'
    database = 'database' 
    username = 'username' 
    password = 'password'

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # set up the cursor
    cursor = cnxn.cursor()

    # Query 
    query = "query"

    cursor.execute(query)
    cnxn.commit()

    return 'done'