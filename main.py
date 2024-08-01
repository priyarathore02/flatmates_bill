from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Enter amount: "))
period = input("Enter period: ")
name1 = input("Enter first flatmate name: ")
days_in_house1 = int(input(f"Enter number of days did {name1} stayed in house: "))
name2 = input("Enter second flatmate name: ")
days_in_house2 = int(input(f"Enter number of days did {name2} stayed in house: "))


the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ",flatmate1.pays(the_bill,flatmate2))
print(f"{name2} pays:",flatmate2.pays(the_bill,flatmate1))

pdf_report = PdfReport(f"{the_bill.period}.pdf")
pdf_report.generate_pdf(flatmate1,flatmate2 , the_bill)







