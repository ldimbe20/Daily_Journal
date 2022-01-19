class Entry():
    """[Creating entry information] """
    
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, entries, concepts, mood_id, date):
        self.id = id #id is the field that stores the id
        self.entries = entries #name is the field that stores the value name
        self.concepts = concepts #breed is the field that stores the value breed
        self.mood_id = mood_id #status is the field that stores field
        self.date = date #location is the field that stores value of location
        self.mood = None
        
# entry_one = Entry(1, "I hope I can do this", "Python", 1, 10/10/22)


