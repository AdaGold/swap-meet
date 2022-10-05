class Item:
    def __init__(self, category = "", condition = 0.0, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        rating_description = {
        0: "Bad",
        1: "Poor",
        2: "Fair",
        3: "Good",
        4: "Very Good",
        5: "Excellent"
        }

        return rating_description[self.condition]
