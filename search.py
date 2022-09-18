class Searcher():
    def __init__(self, data):
        self.data = data
    def parse_guery(self, text):
        value = text.lower().strip()
        return [name for name in self.data if value in name.lower()]