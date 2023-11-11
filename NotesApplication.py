import json
import os
import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NotesApp:
    def __init__(self, notes_file):
        self.notes_file = notes_file
        if not os.path.exists(self.notes_file):
            with open(self.notes_file, 'w') as f:
                json.dump([], f)

    def load_notes(self):
        with open(self.notes_file, 'r') as f:
            return json.load(f)

    def save_notes(self, notes):
        with open(self.notes_file, 'w') as f:
            json.dump(notes, f, default=lambda o: o.__dict__)

    def add_note(self, note_id, title, body):
        notes = self.load_notes()
        timestamp = datetime.datetime.now().isoformat()
        note = Note(note_id, title, body, timestamp)
        notes.append(note.__dict__)
        self.save_notes(notes)

    def read_notes(self):
        notes = self.load_notes()
        for note in notes:
            print(f"ID: {note['note_id']}, Title: {note['title']}, Body: {note['body']}, Timestamp: {note['timestamp']}")

    def update_note(self, note_id, title, body):
        notes = self.load_notes()
        for note in notes:
            if note['note_id'] == note_id:
                note['title'] = title
                note['body'] = body
                note['timestamp'] = datetime.datetime.now().isoformat()
                break
        self.save_notes(notes)

    def delete_note(self, note_id):
        notes = self.load_notes()
        notes = [note for note in notes if note['note_id'] != note_id]
        self.save_notes(notes)

    def view_note(self, note_id):
        notes = self.load_notes()
        for note in notes:
            if note['note_id'] == note_id:
                print(f"ID: {note['note_id']}, Title: {note['title']}, Body: {note['body']}, Timestamp: {note['timestamp']}")
                return
        print("Note not found.")

    def filter_notes_by_date(self, start_date, end_date):
        notes = self.load_notes()
        filtered_notes = [note for note in notes if start_date <= note['timestamp'] <= end_date]
        for note in filtered_notes:
            print(f"ID: {note['note_id']}, Title: {note['title']}, Body: {note['body']}, Timestamp: {note['timestamp']}")

if __name__ == "__main__":
    app = NotesApp('notes.json')
    while True:
        print("1. Добавить заметку")
        print("2. Читать заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Посмотреть заметку")
        print("6. Фильтровать заметки по дате")
        print("7. Выход")
        choice = input("Enter your choice: ")
        if choice == "1":
            note_id = input("Enter note ID: ")
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            app.add_note(note_id, title, body)
        elif choice == "2":
            app.read_notes()
        elif choice == "3":
            note_id = input("Enter note ID to update: ")
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            app.update_note(note_id, title, body)
        elif choice == "4":
            note_id = input("Enter note ID to delete: ")
            app.delete_note(note_id)
        elif choice == "5":
            note_id = input("Enter note ID to view: ")
            app.view_note(note_id)
        elif choice == "6":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            app.filter_notes_by_date(start_date, end_date)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")