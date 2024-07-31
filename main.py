class Bill():
    """
    contains data of bill like amount and period.
    """
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period
class Flatmate():
    """
    details of each flatmate related to number of days stayed
    and sharing of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill,other_flatmate):
        weight = self.days_in_house/(self.days_in_house + other_flatmate.days_in_house)
        to_pay=  weight*bill.amount
        return to_pay

class PdfReport():
    """
    generates pdf file of each flatmate about the amount that
    they have to pay.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1,flatmate2):
        pass

the_bill = Bill(amount=120,period="July 2024")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print("john pays: ",john.pays(bill=the_bill,other_flatmate= marry))
print("marry pays:",marry.pays(bill=the_bill,other_flatmate= john))








