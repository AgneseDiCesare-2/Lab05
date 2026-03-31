import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def cercaIscritti(self):
        pass

    def cercaStudente(self):
        pass

    def cercaCorso(self):
        pass

    def iscrivi(self):
        pass

    #per riempire il menù a tendina
    def riempiDropdown(self): #non posso farlo nella view, devo leggere il database! LO METTO NEL MODELLO
        for corso in self._model.getAllCorsi():
            self._view._corsi.options.append(ft.Dropdown.Option(key=corso.codins, text=corso.__str__()))
        return self._view._corsi #credo ?
