from swap_meet.item import Item

class Clothing(Item):
    def __init__(self,id = 0, fabric = "Unknown", condition = 0, age=0):
        super().__init__(id , condition,age)
        self.fabric = fabric
    
    def __str__(self):
        str1 = super().__str__()
        str2 = f"It is made from {self.fabric} fabric."
        return str1 + " " + str2