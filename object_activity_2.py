class veicle:
    def _init_(self, maxspeed, milage):
        self.maxspeed = maxspeed
        self.milage = milage
ob = veicle()
ob._init_(240, 18)
print("maximum speed ", ob.maxspeed)
print("milage ", ob.milage)