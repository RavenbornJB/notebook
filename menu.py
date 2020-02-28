import sys
from notebook import Note, Notebook


class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    @staticmethod
    def display_menu():
        print("""
    Notebook Menu
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Quit
    """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option number: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid option.')

    def show_notes(self, notes=None):
        if notes is None:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}: {note.tags}\n{note.memo}')

    def search_notes(self):
        check = input("Search for: ")
        notes = self.notebook.search(check)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        note_id = input("Enter a note id: ")
        memo = input("Enter a new memo (press Enter to skip): ")
        tags = input("Enter new tags (press Enter to skip): ")
        if memo:
            self.notebook.modify_memo(note_id, memo)
        if tags:
            self.notebook.modify_tags(note_id, tags)

    @staticmethod
    def quit():
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
