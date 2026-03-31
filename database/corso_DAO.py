# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection

#statico
from database import DB_connect
from model.corso import Corso

class DAO:

    @staticmethod
    def getCodins():
        cnx = DB_connect.get_connection()

        cursor = cnx.cursor(dictionary=True)
        query = "select codins from corso"
        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(row["codins"]) #è un dizionario --> salvo codins

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        cnx = DB_connect.get_connection()

        cursor = cnx.cursor(dictionary=True)
        query = "select * from corso" #restituisce un dizionario con chiave codiceCorso
        cursor.execute(query)

        res = []
        for row in cursor:
            nuovo=Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            res.append(nuovo)
            res.append(row["codins"])  # è un dizionario --> salvo codins

        cursor.close()
        cnx.close()
        return res
