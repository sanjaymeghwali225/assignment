#Ques1
n1=int(input())
n2=int(input())
n3=int(input())
average=(n1+n2+n3)/3
print(average)
#Ques2
Gross_income=(input("Enter your gross income"))
print("Enter no.of dependents")
number_of_dependents=input()
Taxable_income=float(Gross_income)-10000-3000*float(number_of_dependents)
Tax=Taxable_income*20/100
print(f"Tax={Tax}")
#Ques3
time = int(input("no. of seconds = "))
minute = int(time/60)
sec = time%60
print("time is equal to", minute,"minutes and", sec, "seconds")
#Ques4
a = 25+int('25')+25.0
b = str(a)

print(b)
#Ques5
from math import *

for i in range(0,360,15):
    print(i, '---', round(sin(i),4), round(cos(i),4) )

