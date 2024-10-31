






class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = int(age)
        self.address = address 

    def display_person_info(self): 
        return f"""
        Name: {self.name}
        Age: {self.age}
        Address: {self.address}"""