import flet as ft

import database.studente_DAO as studente_DAO
import database.corso_DAO as corso_DAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.corsoSelezionato = None
        #self.matricola=None

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

        self._view.lvOut.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso: "))
        for s in iscritti:
            self._view.lvOut.controls.append(ft.Text(str(s)))
        self._view.update_page()

    def cercaStudente(self, e):
        #scritta la matricola deve completare automaticamente nome e cognome
        matricola=self._view.txt_matricola.value

        if matricola=="":
            (self._view.create_alert("Attenzione, devi selezionare un corso!"))
            self._view.update_page()
            return

        studente=studente_DAO.cercaStudente(matricola) #restituisce lo studente cercato
        self._view.lvOut.controls.clear()

        self._view.txt_nome.value = studente.nome
        self._view.txt_cognome.value = studente.cognome
        self._view.update_page()

    def cercaCorso(self, e):
        matricola=self._view.txt_matricola.value

        if matricola == "":
            self._view.create_alert("Attenzione, devi inserire una matricola!")
            return

        #delego la ricerca al DAO
        corsi=corso_DAO.getCorsiStudente(matricola) #lista

        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(ft.Text(f"Risultano {len(corsi)} corsi: "))

        for corso in corsi:
            self._view.lvOut.controls.append(ft.Text(str(corso)))
        self._view.update_page()
        pass

    def iscrivi(self, e):
        matricola=self._view.txt_matricola.value
        codins=self._view._corsi.value
        if matricola=="" or codins=="":
            self._view.create_alert("Attenzione, devi inserire una matricola e un codice corso!")

        #controllo che lo studente inserito sia presente nel database
        studente = studente_DAO.cercaStudente(matricola)
        if studente is None:

            self._view.create_alert("Attenzione, la matricola inserita non esiste!")
        esito=corso_DAO.iscrivi(matricola, codins)
        self._view.lvOut.controls.clear()

        if esito:
            self._view.create_alert("Studente iscritto correttamente")
        else:
            self._view.create_alert("Errore nell'iscrizione")

    #per riempire il menù a tendina
    def riempiDropdown(self): #non posso farlo nella view, devo leggere il database! LO METTO NEL MODELLO
        for corso in self._model.getAllCorsi():
            self._view._corsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        return self._view._corsi #credo ?
