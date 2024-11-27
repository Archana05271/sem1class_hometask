#employee
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(f"Name:{self.name}\nSalary:{self.salary}")
class Manager(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def show(self):
        self.display_details()
        print(f"Department:{self.dept}")
s=Manager("Amal",25000,"Engineer")
s.show()
#Library
class Libraryitem:
    def __init__(self,title,author,pub_year):
        self.title=title
        self.author=author
        self.pub_year=pub_year
    def display_info(self):
        print(f"Title:{self.title}\nAuthor:{self.author}\nPublication year:{self.pub_year}")
class Book(Libraryitem):
    def __init__(self,title,author,pub_year,genre):
        super().__init__(title,author,pub_year)
        self.genre=genre
    def show(self):
        self.display_info()
        print(f"Genre:{self.genre}")
s=Book("It Starts With Us","Colleen Hoover",2022,"Romantic")
s.show()
#bank
class BankAccount:
    def __init__(self,ini_bal):
        self.ini_bal=ini_bal
    def deposit(self):
        a=int(input("Money to deposit:"))
        self.ini_bal=self.ini_bal+a
        print("Amount deposited")
    def withdraw(self):
        b=int(input("Money to withdraw:"))
        self.ini_bal=self.ini_bal-b
        print("Amount Withdrawn")
    def c_bal(self):
        print(f"Balance:{self.ini_bal}")
cus=BankAccount(25000)
cus.deposit()
cus.withdraw()
cus.c_bal()
