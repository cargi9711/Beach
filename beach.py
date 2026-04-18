class Beach:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def describe(self):
        return f"{self.name} is a beautiful beach located in {self.location}."

    def __str__(self):
        return f"{self.name} ({self.location})"
