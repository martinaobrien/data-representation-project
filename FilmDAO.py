import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor


class FilmDao:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        #print ("connection made")

    def create(self, film):
        cursor = self.db.cursor()
        sql = "insert into films (Id, Film, Director, Year) values (%s,%s,%s,%s)"
        values = [
            film['Id'],
            film['Film'],
            film['Director'],
            film['Year']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from films'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, Id):
        cursor = self.db.cursor()
        sql = 'select * from films where Id = %s'
        values = [Id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, film):
        cursor = self.db.cursor()
        sql = "update films set Film = %s, Director = %s, Year = %s where Id = %s"
        values = [
            film['Film'],
            film['Director'],
            film['Year'],
            film['Id']

        ]
        cursor.execute(sql, values)
        self.db.commit()
        return film

    def delete(self, Id):
        cursor = self.db.cursor()
        sql = 'delete from films where Id = %s'
        values = [Id]
        cursor.execute(sql, values)
        self.db.commit()
        return {}

    def convertToDict(self, result):
        colnames = ['Id', 'Film', 'Director', 'Year']
        film = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                film[colName] = value
        return film


filmDao = FilmDao()