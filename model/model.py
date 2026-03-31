from database import corso_DAO


class Model:
    def __init__(self):
        pass

    #il modello non lo sa --> lo chiede al DAO
    def getCodins(self):
        return corso_DAO.getCodins()
