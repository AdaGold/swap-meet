import uuid

# unique_id = int(uuid.uuid4())
# print(unique_id)

class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            id = int(uuid.uuid4())
        self.id = id
        self.condition = condition

    def get_category(self):
        return type(self).__name__
        #return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Terrible: Unusable, broken, contaminated, or carries the possessed spirit of its previous owner. One might question why this was even considered sellable."
        if self.condition == 1:
            return "Poor: High likelihood of abnormalities, defects, or irremovable stains you probably don't want to know about. Probably best to scavenge for parts."
        if self.condition == 2:
            return "As-Is: Acceptable but of course, that's subjective. Consider at your own discretion."
        if self.condition == 3:
            return "Good: Functional or wearable. What more could you ask for a discounted price?"
        if self.condition == 4:
            return "Gently Worn: Practically like new. It's basically a steal. At least it's not cursed."
        if self.condition == 5:
            return "New: Pretty much in pristine condition with the added bonus of attracting cats and good luck. Great for gifting to others at a bargain."