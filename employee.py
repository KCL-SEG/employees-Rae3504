"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Salary:
	def __init__(self, salary):
		self.salary = salary

	def __str__(self):
		return f"monthly salary of {self.salary}"

	def get_pay(self):
		return self.salary

class Contract:
	def __init__(self, hours, wage):
		self.hours = hours
		self.wage = wage

	def __str__(self):
		return f"contract of {self.hours} hours at {self.wage}/hour"

	def get_pay(self):
		return self.hours * self.wage

class ContractCommission:
	def __init__(self, amount, commission):
		self.amount = amount
		self.commission = commission

	def __str__(self):
		return f"commission for {self.amount} contract(s) at {self.commission}/contract"

	def get_pay(self):
		return self.amount * self.commission

class BonusCommission:
	def __init__(self, bonus):
		self.bonus = bonus

	def __str__(self):
		return f"bonus commission of {self.bonus}"

	def get_pay(self):
		return self.bonus

class Employee:
	def __init__(self, name, *payments):
		self.name = name
		self.payments = payments

	def get_pay(self):
		total = 0
		for payment in self.payments:
			total += payment.get_pay()
		return total

	def __str__(self):
		string = self.name
		for i, payment in enumerate(self.payments):
			if i == 0:
				string += " works on a "
			else:
				string += " and receives a "

			string += str(payment)
		string += f". Their total pay is {self.get_pay()}."
		return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Salary(4000))
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract(100, 25))
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Salary(3000), ContractCommission(4, 200))
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract(150, 25), ContractCommission(3, 220))
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Salary(2000), BonusCommission(1500))
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract(120, 30), BonusCommission(600))
print(str(ariel))