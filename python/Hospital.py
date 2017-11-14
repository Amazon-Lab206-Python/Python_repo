class Patient(object):
    id_counter = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        