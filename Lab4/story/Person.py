class Person:
    moods = ("happy", "tired", "lazy") 

    def __init__(self, name, money=500, mood="happy", healthRate=100):
        self.name       = name
        self.money      = money
        self.mood       = mood
        self.healthRate = healthRate

 
    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        self._healthRate = max(0, min(100, value))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        print(f"{self.name} slept {hours}h  mood: {self.mood}")

    def eat(self, meals):
        if meals >= 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        else:
            self.healthRate = 50
        print(f"{self.name} ate {meals} meal(s) health: {self.healthRate}%")

    def buy(self, items):
        cost = items * 10
        self.money -= cost
        print(f"{self.name} bought {items} item(s), spent {cost} L.E money left: {self.money} L.E")

    def display(self):
        print(f"Person: {self.name}, Mood: {self.mood}, Health: {self.healthRate}%")
