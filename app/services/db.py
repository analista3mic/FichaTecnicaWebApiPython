from config import get_db_connection

def execute_stored_procedure(sp_name, params):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.callproc(sp_name, params)
    
    results = []
    for result in cursor.stored_results():
        results = result.fetchall()

    cursor.close()
    connection.close()
    
    return results
