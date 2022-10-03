# from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, category = None):
        self.category = category if category is not None else ""