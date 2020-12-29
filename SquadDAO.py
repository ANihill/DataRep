import mysql.connector
import dbconfig as cfg

class SquadDAO:
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

    def create(self, player):
        cursor = self.db.cursor()
        sql = "insert into squad (playerNumber, playerName, position, age) values (%s,%s,%s,%s)"
        values = [
            player['playerNumber'],
            player['playerName'],
            player['position'],
            player['age']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from squad'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, squadNumber):
        cursor = self.db.cursor()
        sql = 'select * from squad where playerNumber = %s'
        values = [ squadNumber ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, player):
        cursor = self.db.cursor()
        sql = "update squad set playerName = %s, position = %s, age = %s where playerNumber = %s"
        values = [
            player['playerName'],
            player['position'],
            player['age'],
            player['playerNumber']

        ]
        cursor.execute(sql, values)
        self.db.commit()
        return player

    def delete(self, playerNumber):
        cursor = self.db.cursor()
        sql = 'delete from squad where playerNumber = %s'
        values = [playerNumber,]
        cursor.execute(sql, values)
        self.db.commit()
        return {}



    def convertToDict(self, result):
        colnames = ['playerNumber','playerName', 'position', 'age']
        player = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                player[colName] = value
        return player

squadDAO = SquadDAO()
