from datetime import datetime
class Note:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"
class Notebook:
    def __init__(self):
        self.notes: list[Note] = []
    def add_note(self, title: str, text: str, importance: str) -> int:
        if not self.notes:
            new_code = 1
        else:
            new_code = max(int(note.code) for note in self.notes) + 1
        new_note = Note(str(new_code), title, text, importance)
        self.notes.append(new_note)
        return new_code
    def delete_note(self, code: int):
        self.notes = [n for n in self.notes if n.code != str(code)]
    def important_notes(self) -> list[Note]:
        return [n for n in self.notes if n.importance in [Note.HIGH, Note.MEDIUM]]
    def notes_by_tag(self, tag: str) -> list[Note]:
        return [n for n in self.notes if tag in n.tags]
    def tag_with_most_notes(self) -> str:
        tag_counts = {}
        for note in self.notes:
            for tag in note.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        if not tag_counts:
            return "NO ETIQUETAS FOR YOU"
        max_freq = max(tag_counts.values())
        best_tags = sorted([tag for tag, count in tag_counts.items() if count == max_freq])
        return best_tags[0]