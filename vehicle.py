class Vehicle:
    def __init__(self, color):
        self.name = "initial name"
        self.color = color

    def drive(self):
        print("zoom")

    def turn(self, direction):
        print(f'turn {direction}.')

    def stop(self):
        print("stops normally.")

    def new_name(self, name):
        self.name = name