import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.lvOut = None
        self.btn_iscrivi = None
        self.btn_cercaStudente = None
        self.btn_cercaCorsi = None
        self.txt_cognome = None
        self.txt_nome = None
        self.btn_cercaIscritti = None
        self._corsi = None
        self.txt_matricola = None
        
        
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)


        #ROW with some controls
        #menù a tendina corsi
        self._corsi = ft.Dropdown.Option(key=corso.codins, text=corso.__str__())
        self.controller.riempiDropdown()
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.cercaIscritti)
        row1 = ft.Row(controls=[self._corsi, self.btn_cercaIscritti], alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row1)

        # text field for the name, surname and student code
        self.txt_matricola = ft.TextField(
            label="",
            width=200,
            hint_text="matricola"
        )

        self.txt_nome = ft.TextField(
            label="",
            width=200,
            hint_text="nome",
            read_only=True
        )

        self.txt_cognome = ft.TextField(
            label="",
            width=200,
            hint_text="cognome",
            read_only=True
        )
        row2 = ft.Row(controls=[self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row2)

        #terza riga
        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.cercaStudente)
        self.btn_cercaCorsi = ft.ElevatedButton(text="Cerca Corso", on_click=self._controller.cercaCorso)
        self.btn_iscrivi = ft.ElevatedButton(text="Cerca Iscrivi", on_click=self._controller.iscrivi)
        row3 = ft.Row(controls=[self.btn_cercaStudente, self.btn_cercaCorsi, self.btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row3)

        # List View where the reply is printed (lvOut)
        self.lvOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lvOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
