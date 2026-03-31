# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from dataclasses import dataclass

@dataclass
class corso_DAO:
    codins: str
    crediti: int
    nome: str
    pd: int

    def __hash__(self):
        return hash(self.codins)

    def __eq__(self, other):
        return self.codins == other.codins

    def __str__(self):
        return f"{self.nome} ({self.codins})"

