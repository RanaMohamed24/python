from Car     import Car
from Employee import Employee
from Office  import Office


fiat128 = Car(name="Fiat 128", fuelRate=100)

samy = Employee(
    emp_id         = 1,
    name           = "Samy",
    email          = "samy@iti.eg",
    salary         = 5000,
    distanceToWork = 20,
    money          = 1000,
    car            = fiat128,
)

iti = Office(name="ITI Smart Village")
iti.hire(samy)

samy.display()
fiat128.display()
iti.display()



samy.sleep(7)     
samy.eat(3)      
samy.work(8)    
samy.buy(2)      




samy.drive(20)    
samy.refuel(50)  




iti.check_lateness(samy.id, move_hour=8)


iti.reward(samy.id, 500)
iti.deduct(samy.id, 100)


print("\nAll employees:")
for emp in iti.get_all_employees():
    emp.display()




samy.send_mail(
    to            = "manager@iti.eg",
    subject       = "Hello",
    msg           = "This is a test email from Samy.",
    receiver_name = "Manager",
)




iti.save_to_json("iti_office.json")