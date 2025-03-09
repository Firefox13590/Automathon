from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Aide->A propos du Bloc-notes")
app.AProposDuBlocNotes.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
