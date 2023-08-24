import pandas as pd
from sqlalchemy import create_engine

def extraer_tabla():
    """
    Extraer la tabla table_name de SQL server
    
    Arguments:
    
    Outputs: table_name
    """

    # Credenciales
    server = 'servidor'
    database = 'base_de_datos' 
    username = 'usuario' 
    password = 'contraseña'
    
    # Create a SQLAlchemy engine object
    engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=SQL+Server')
    query = "SELECT * FROM table_name;"

    return pd.read_sql(query, engine)