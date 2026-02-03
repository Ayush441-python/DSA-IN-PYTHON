class Programmer:
    company = "Microsoft"  # Class variable

    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Language: {self.language}")
        print(f"Salary: ₹{self.salary}\n")


# Creating objects
p1 = Programmer("Ayush", "Python", 120000)
p2 = Programmer("Ravi", "Java", 100000)
p3 = Programmer("Sneha", "C++", 110000)

# Printing info
p1.getInfo()
p2.getInfo()
p3.getInfo()





 
