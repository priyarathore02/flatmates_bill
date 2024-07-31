import webbrowser

from fpdf import FPDF
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

    def generate_pdf(self, flatmate1,flatmate2,bill):
        f1_pay = str(round(flatmate1.pays(bill,flatmate2),2))
        f2_pay = str(round(flatmate2.pays(bill,flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #add icon
        pdf.image("house.png",w=30,h=30)

        #insert title
        pdf.set_font('Arial', 'B', size=12)
        pdf.cell(0, 80, 'FLATMATES BILL', border=1, align='C', ln=1)

        # insert period value
        pdf.cell(w=100, h=40, txt='PERIOD:', border=1)
        pdf.cell(w=100, h=40, txt= bill.period , border=1,ln=1)

        #insert name and amount that will be paid by flatmate 1.
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=40, txt= f1_pay , border=1,ln=1)

        # insert name and amount that will be paid by flatmate 2.
        pdf.cell(w=100, h=40, txt= flatmate2.name, border=1)
        pdf.cell(w=100, h=40, txt=f2_pay, border=1, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)

the_bill = Bill(amount=120,period="July 2024")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print("john pays: ",john.pays(bill=the_bill,other_flatmate= marry))
print("marry pays:",marry.pays(bill=the_bill,other_flatmate= john))

pdf_report = PdfReport(filename= "flatmates.pdf")
pdf_report.generate_pdf(flatmate1= john,flatmate2= marry,bill= the_bill)







