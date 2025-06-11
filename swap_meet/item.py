import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        self.id = int(uuid.uuid4()) if id is None else id
        self.condition = condition

    def get_category(self):
        return type(self).__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        condition_rating = {
            0: "Terrible: Unusable, broken, contaminated, or carries the possessed spirit of its previous owner. One might question why this was even considered sellable.",
            1: "Poor: High likelihood of abnormalities, defects, or irremovable stains you probably don't want to know about. Probably best to scavenge for parts.",
            2: "As-Is: Acceptable but of course, that's subjective. Consider at your own discretion.",
            3: "Good: Functional or wearable. What more could you ask for a discounted price?",
            4: "Gently worn: Practically like new. It's basically a steal. At least it's not cursed.",
            5: "New: Pretty much in pristine condition with the added bonus of preventing existential crises and attracting good luck."
        }
        return condition_rating[self.condition]