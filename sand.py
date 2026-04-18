class Sand:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture

    def feel(self):
        return f"The sand is {self.texture} and {self.color} in color."
