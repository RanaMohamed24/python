class Car:
    def __init__(self, name, fuelRate=100, velocity=0):
        self.name     = name
        self.fuelRate = fuelRate
        self.velocity = velocity

  
    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = max(0, min(100, value))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = max(0, min(200, value))

    def run(self, velocity, distance):
        self.velocity = velocity
     
        fuel_decrease = (distance // 10) * 10
        self.fuelRate -= fuel_decrease

        if self.fuelRate <= 0:
            km_done  = (distance // 10) * 10
            remain   = distance - km_done
            self.stop(remain)
        else:
            self.stop(0)

    def stop(self, remain_distance=0):
        self.velocity = 0
        if remain_distance > 0:
            print(f"[{self.name}] Out of fuel! Remaining: {remain_distance} km")
        else:
            print(f"[{self.name}] Arrived !")

    def to_dict(self):
        return {
            "name":     self.name,
            "fuelRate": self.fuelRate,
            "velocity": self.velocity,
        }

    def display(self):
        print(f"Car: {self.name}, Fuel: {self.fuelRate}%, Speed: {self.velocity} km/h")
