class SessionMemory:
    def __init__(self):
        self.history = []

    def add_entry(self, query, result):
        self.history.append({"query": query, "result": result})

    def get_history(self):
        return self.history