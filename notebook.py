from datetime import date
from exceptions import NoteNotFound


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched."""

    def __init__(self):
        """Initialize a notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        note = self._find_note(note_id)
        if note is None:
            raise NoteNotFound(f'The note with ID of {note_id} does not exist')
        note.memo = memo

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        note = self._find_note(note_id)
        if note is not None:
            note.tags = tags

    def search(self, check):
        """Find all notes that match the given filter
        string."""
        return [note for note in self.notes if note.match(check)]


class Note:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    note_ids = 0

    def __init__(self, memo, tags=''):
        """Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""
        self.memo = memo
        self.creation_date = date.today()
        self.tags = tags
        self.id = self.note_ids
        self.note_ids += 1

    def match(self, check):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags."""
        return check in self.memo or check in self.tags
