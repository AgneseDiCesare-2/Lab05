import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def cercaIscritti(self, e):
        pass

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
