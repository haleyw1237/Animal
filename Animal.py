class Animal:
    
    animal_type = None
    name = None
    mood = None

    def __init__(self, animal_type, name, mood):
        self.animal_type = animal_type
        self.name = name
        self.mood = mood
	
    def get_animal_type(self):
        return self.animal_type

    def get_name(self):
        return self.name

    def get_mood(self):
        return self.mood
	
    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_name(self, name):
        self.name = name

    def set_mood(self, mood):
        self.mood = mood