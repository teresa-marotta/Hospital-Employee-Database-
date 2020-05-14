class Employee:
	
	def __init__(self, first, last, dept, pay, ext):
		self.first = first
		self.last = last
		self.dept = dept 
		self.pay = pay 
		self.ext = ext 

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.dept, self.pay)

		
		