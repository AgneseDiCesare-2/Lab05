import flet as ft

import database.studente_DAO
from database import studente_DAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.corsoSelezionato = None
        self.matricola=None

        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def cercaIscritti(self, e):
        self.corsoSelezionato= self._view._corsi.value#riconsce il corso selezionato nel dropdown

        #ALERT NON FUNZIONA :-((
        if self.corsoSelezionato is None:
            self._view.create_alert("Attenzione, devi selezionare un corso!")
            self._view.update_page()
            return
        #se ho selezionato un corso devo fare una query al database per trovare gli iscritti al corso
        iscritti=studente_DAO.get_iscritti(self.corsoSelezionato)
        self._view.lvOut.controls.clear()

        for s in iscritti:
            self._view.lvOut.controls.append(ft.Text(str(s)))
        self._view.update_page()

    def cercaStudente(self, e):
        #scritta la matricola deve completare automaticamente nome e cognome
        self.matricola=self._view.txt_matricola.value

        if self.matricola is None:
            self._view.create_alert("Attenzione, devi selezionare un corso!")
            self._view.update_page()
            return
        studente=database.studente_DAO.cercaStudente(self.matricola) #restituisce lo studente cercato
        self._view.lvOut.controls.clear()

        self._view.txt_nome.value = studente.nome
        self._view.txt_cognome.value = studente.cognome

    def cercaCorso(self, e):
        pass

    def iscrivi(self, e):
        pass

    #per riempire il menù a tendina
    def riempiDropdown(self): #non posso farlo nella view, devo leggere il database! LO METTO NEL MODELLO
        for corso in self._model.getAllCorsi():
            self._view._corsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        return self._view._corsi #credo ?
