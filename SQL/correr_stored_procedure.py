import pyodbc

def run_stored_procedure(param):
    """
    Correr stored procedure con parametro 'param'

    Arguments: parametro para el stored procedure
    
    Outputs: 
    """
    # set up the connection to the database
    server = 'server' 
    database = 'database' 
    username = 'username' 
    password = 'password'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # set up the cursor
    cursor = cnxn.cursor()

    # call the stored procedure with the provided parameter 
    params = (param,)
    try:
        cursor.execute("{CALL stored_procedure(?)}", params)
        cnxn.commit()
    except Exception as e:
        print(f"Error calling stored procedure: {e}")
    finally:
        # close the cursor and the connection
        cursor.close()
        cnxn.close()

    return 'done'