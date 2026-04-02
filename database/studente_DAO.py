# Add whatever it is needed to interface with the DB Table studente
from database import DB_connect
from model.studente import StudentDAO


@staticmethod
def get_iscritti(codins):
    cnx = DB_connect.get_connection()

    cursor = cnx.cursor(dictionary=True)
    query = """select s.*
            from iscrizione i, studente s
            where i.matricola = s.matricola AND i.codins=%s """
    cursor.execute(query, (codins,))
    #restituisce i dati degli gli studenti

    res = []
    for row in cursor:
        res.append(StudentDAO(**row))  #metodo standard quando le colonne del database hanno lo stesso nome dei campi dell'oggetto
        #posso convertire automaticamente le row

    cursor.close()
    cnx.close()
    return res

@staticmethod
def cercaStudente(matricola):
    cnx = DB_connect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """select s.*"""
    query = """select *
                from studente
                where matricola = %s"""
    cursor.execute(query, (matricola,))
    # restituisce i dati dello studente --> mi aspetto un solo studente
    row=cursor.fetchone()
    if row is None:
        return

    res=(StudentDAO(**row))

    cursor.close()
    cnx.close()
    return res


