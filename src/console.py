from src.notebook import Notebook, Note


class ConsoleUI:
    def __init__(self):
        self.notebook = Notebook()

    def show_menu(self):
        print("\n--- CUADERNO DE NOTAS suyo =) ---")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Agregar etiqueta a nota")
        print("4. Listar notas importantes")
        print("5. Eliminar nota")
        print("6. Mostrar notas por etiqueta")
        print("7. Mostrar etiqueta con más notas")
        print("8. Salir")

    def add_note_ui(self):
        title = input("Título: ")
        text = input("Contenido: ")
        print("Importancia: 1. HIGH, 2. MEDIUM, 3. LOW")
        op = input("Seleccione (1-3): ")
        imp = Note.LOW
        if op == "1":
            imp = Note.HIGH
        elif op == "2":
            imp = Note.MEDIUM

        code = self.notebook.add_note(title, text, imp)
        print(f"Nota agregada con éxito. ID: {code}")

    def list_notes(self, notes_list=None):
        notes = notes_list if notes_list is not None else self.notebook.notes
        if not notes:
            print("No notas to show.")
        for n in notes:
            print(f"\nID: {n.code} | Importancia: {n.importance} | Tags: {n.tags}")
            print(n)

    def add_tag_ui(self):
        code = input("ID de la nota: ")
        tag = input("New etiqueta: ")
        found = False
        for n in self.notebook.notes:
            if n.code == code:
                n.add_tag(tag)
                print("Etiqueta agregada.")
                found = True
                break
        if not found: print("Nota no encontrada.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select a option: ")
            if choice == "1":
                self.add_note_ui()
            elif choice == "2":
                self.list_notes()
            elif choice == "3":
                self.add_tag_ui()
            elif choice == "4":
                self.list_notes(self.notebook.important_notes())
            elif choice == "5":
                code = int(input("ID to kill: "))
                self.notebook.delete_note(code)
                print("Operación realized .")
            elif choice == "6":
                tag = input("Etiqueta to search: ")
                self.list_notes(self.notebook.notes_by_tag(tag))
            elif choice == "7":
                print(f"the most used etiqueta: {self.notebook.tag_with_most_notes()}")
            elif choice == "8":
                print("BYEEE")
                break
            else:
                print("INVALIDA OPTION.")