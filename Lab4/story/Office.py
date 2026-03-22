import json


class Office:
    employeesNum = 0   

    def __init__(self, name):
        self.name      = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum += num

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.change_emps_num(1)
        print(f"{employee.name} hired at {self.name}. Total: {Office.employeesNum}")

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.change_emps_num(-1)
            print(f"{emp.name} fired from {self.name}. Total: {Office.employeesNum}")
        else:
            print(f"Employee {emp_id} not found.")

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction
            print(f"Deducted {deduction} from {emp.name}. New salary: {emp.salary}")

    def reward(self, emp_id, reward_amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward_amount
            print(f"Rewarded {emp.name} +{reward_amount}. New salary: {emp.salary}")

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if not emp:
            print("Employee not found.")
            return
        is_late = Office.calculate_lateness(9, move_hour, emp.distanceToWork, velocity=60)
        if is_late:
            print(f"{emp.name} is LATE! Deducting 10.")
            self.deduct(emp_id, 10)
        else:
            print(f"{emp.name} is ON TIME! Rewarding 10.")
            self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        """Returns True if late, False if on time."""
        travel_time = distance / velocity
        arrival     = move_hour + travel_time
        return arrival >= target_hour

    def save_to_json(self, filename="iti_office.json"):
        data = {
            "office":    self.name,
            "employees": [emp.to_dict() for emp in self.employees],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Office data saved  '{filename}'")

    def display(self):
        print(f"Office: {self.name}, Employees: {len(self.employees)}")