from sqlalchemy import create_engine

def subir_tabla(df):
    """
    Concatenar df en table_name
    
    Arguments: df, dataframe 
    
    Outputs: Concatena en table_name
    """
    
    # Credenciales
    server = 'servidor'
    database = 'base_de_datos' 
    username = 'usuario' 
    password = 'contraseña'

    # Crea un objeto engine SQLAlchemy
    engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=SQL+Server',use_setinputsizes=False)

    # Definir tabla donde se concatena el df
    table_name = 'table_name'

    return df.to_sql(table_name, engine, if_exists='append', index=False)