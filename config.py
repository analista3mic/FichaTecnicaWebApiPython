import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host="db-mysql-nyc3-55483-do-user-16878996-0.f.db.ondigitalocean.com",
        port=25060,
        user="doadmin",
        password="AVNS_f_dKi3vtkK7WJ6r-8Vh",
        database="FichaTecnica"
    )
