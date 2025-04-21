from flask_mysqldb import MySQL
from flask import Flask
from config import Config

mysql = MySQL()

def init_db(app: Flask):
    app.config["MYSQL_HOST"] = Config.MYSQL_HOST
    app.config["MYSQL_PORT"] = Config.MYSQL_PORT
    app.config["MYSQL_USER"] = Config.MYSQL_USER
    app.config["MYSQL_PASSWORD"] = Config.MYSQL_PASSWORD
    app.config["MYSQL_DB"] = Config.MYSQL_DB
    mysql.init_app(app)
