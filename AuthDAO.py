import mysql.connector
from mysql.connector import cursor
import authdbconfig as cfg


class AuthDAO:
    db = ""

    def initConnectToDB(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self):
        db = self.initConnectToDB()


    def login(self, username, password):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM accounts WHERE username = %s AND password = %s'
        values = [username, password]
        cursor.execute(sql, values)
        account = cursor.fetchone()
        return account

    def checkUser(self, username):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM accounts WHERE username = %s'
        values = [username]
        cursor.execute(sql, values)
        account = cursor.fetchone()
        return account


    def register(self, username, password):
        cursor = self.db.cursor()
        sql = "insert into accounts (username, password) values (%s,%s)"
        values = [username, password]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

authDAO = AuthDAO()
