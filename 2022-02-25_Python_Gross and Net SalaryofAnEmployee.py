#Gross and Net Salary of an employee
#Computer Programming Tutor- Feb 25, 2022
"DA= 18%xBasic"
"HRA=15%xBasic"
"PF=9%xBasic"
"TA=7.5%xBasic"
"Net Pay = Basic + DA +HRA + TA"
"Gross Pay = NetPay- PF"

print("ERNIE'S PYTHON EMPLOYEE SALARY PROGRAM")

Name = str(input("Enter Employee Name:"))
Basic =float(input("Enter Basic Salary:"))
Da=float(Basic*0.18)
Hra=float(Basic*0.12)
Pf=float((Basic + Da)*0.09)
Ta=float(Basic*0.075)
Netpay=float(Basic +Da + Hra+ Ta)
Grosspay=float(Netpay - Pf)


print("\nEMPLOYEE WAGE SLIP")

print("-------------------------------")

print("EMPLOYEE NAME :",Name)
print("BASIC SALARY :",Basic)
print("DEARNESS ALLOWANCE :",Da)
print("HOUSE RENT ALLOWANCE :",Hra)
print("TRAVEL ALLOWANCE :",Ta)

print("-------------------------")

print("NET SALARY PAY:",Netpay)
print("PROVIDEND FUND:",Pf)

print("------------------------------")
print("GROSS PAYMENT:",Grosspay)

print("--------------xxxx---------------")
