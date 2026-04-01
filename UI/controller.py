import flet as ft
from database import studente_DAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def cercaIscritti(self, e):
        corsoSelezionato=e.control.data #e.control.data riconsce il corso selezionato nel dropdown

        if corsoSelezionato is None:
            self._view.create_alert("Attenzione, devi selezionare un corso!")
            self._view.update_page()
            return
        #se ho selezionato un corso devo fare una query al database per trovare gli iscritti al corso
        iscritti=studente_DAO.get_iscritti(corsoSelezionato)

        for s in iscritti:
            self._view.lvOut.controls.append(ft.Txt(s.__str__()))

    def cercaStudente(self, e):
        pass

    def cercaCorso(self, e):
        pass

    def iscrivi(self, e):
        pass

    #per riempire il menù a tendina
    def riempiDropdown(self): #non posso farlo nella view, devo leggere il database! LO METTO NEL MODELLO
        for corso in self._model.getAllCorsi():
            self._view._corsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        return self._view._corsi #credo ?
