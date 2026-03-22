import re
from Person import Person


class Employee(Person):
    def __init__(self, emp_id, name, email, salary,
                 distanceToWork=20, money=500, mood="happy",
                 healthRate=100, car=None):
        super().__init__(name, money, mood, healthRate)
        self.id             = emp_id
        self.email          = email
        self.salary         = salary
        self.distanceToWork = distanceToWork
        self.car            = car

 
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 1000:
            raise ValueError("Salary must be 1000 or more.")
        self._salary = value

 
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email: {value}")
        self._email = value

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        print(f"{self.name} worked {hours}h  mood: {self.mood}")

    def drive(self, distance):
        if self.car is None:
            print(f"{self.name} has no car!")
            return
        velocity = 60  
        print(f"{self.name} driving {distance} km at {velocity} km/h ...")
        self.car.run(velocity, distance)

    def refuel(self, gasAmount=100):
        if self.car is None:
            print(f"{self.name} has no car!")
            return
        self.car.fuelRate += gasAmount
        print(f"Refueled! Fuel now: {self.car.fuelRate}%")

    def send_mail(self, to, subject, msg, receiver_name):
        filename = f"email_{subject.replace(' ', '_')}.txt"
        content = (
            f"From: {self.email}\n"
            f"To: {to}\n\n"
            f"Hi, {receiver_name}\n"
            f"{msg}\n"
            f"thanks"
        )
        with open(filename, "w") as f:
            f.write(content)
        print(f"Email saved : '{filename}'")

    def to_dict(self):
        return {
            "id":             self.id,
            "name":           self.name,
            "email":          self.email,
            "salary":         self.salary,
            "distanceToWork": self.distanceToWork,
            "money":          self.money,
            "mood":           self.mood,
            "healthRate":     self.healthRate,
            "car":            self.car.to_dict() if self.car else None,
        }

def display(self):
    print(f"Employee: {self.name}, ID: {self.id}, Salary: {self.salary}, Mood: {self.mood}")
