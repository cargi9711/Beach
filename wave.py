class Wave:
    def __init__(self, height, temperature):
        self.height = height
        self.temperature = temperature

    def splash(self):
        return f"A wave of {self.height} meters splashes at {self.temperature}°C."
