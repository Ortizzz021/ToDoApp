class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str  = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos: dict[str, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        id = len(self.todos) + 1
        object: Todo = Todo(id, title, description)
        self.todos[id] = object
        return id

    def pending_todos(self) -> list[Todo]:
        return [o for o in self.todos.values() if o.completed]

    def tags_todo_count(self) -> dict[str, int]:
        dict: dict[str, int] = {}

        return dict