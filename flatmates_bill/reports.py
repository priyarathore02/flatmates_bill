import webbrowser

from fpdf import FPDF


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
        pdf.cell(0, 80, 'FLATMATES BILL', border=0, align='C', ln=1)

        # insert period value
        pdf.cell(w=100, h=40, txt='PERIOD:', border=0)
        pdf.cell(w=100, h=40, txt= bill.period , border=0,ln=1)

        #insert name and amount that will be paid by flatmate 1.
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt= f1_pay , border=0,ln=1)

        # insert name and amount that will be paid by flatmate 2.
        pdf.cell(w=100, h=25, txt= flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=f2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)
