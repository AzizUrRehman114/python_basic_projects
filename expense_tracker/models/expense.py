from datetime import datetime

class Expense:
    def __init__(self, amount, category, note, date_time = None):
        self.amount = amount
        self.category = category
        self.note = note
        self.date_time = date_time or datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def to_dict(self):
        dict = {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "date": self.date_time
        }
        return dict