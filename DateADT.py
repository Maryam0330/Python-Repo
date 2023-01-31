#Date ADT
import datetime

class DateADT:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year

    def show_date(self):
        print("Date:",self.date,"/",self.month,"/",self.year)

    def show_day(self):
        return self.date

    def show_month(self):
        return self.month

    def show_year(self):
        return self.year

    def isLeapYear(self):
        return (self.year%4==0)

    def dayOfWeek(self):
               dat=datetime.date(self.year,self.month,self.date)
        return dat.strftime("%A")

mydate=DateADT(10,1,23)
mydate.show_date()
print("Day is",mydate.show_day())
print("Month is",mydate.show_month())
print("Year is",mydate.show_year())
print("Is it a leap year?",mydate.isLeapYear())
print("Day of the week is",mydate.dayOfWeek())
