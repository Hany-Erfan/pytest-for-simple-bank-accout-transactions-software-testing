class Customer:

	def __init__ (self,id):
		if id==123:
			self.personalInfo=Personal("Jennifer",26,"trifftstrasse 40")
			self.bankAccount=BankAccount(7636482684,"aaax73764z")
		elif id==447:
			self.personalInfo=Personal("huewit",29,"bornmannstrasse 30")
			self.bankAccount=BankAccount(4732748223,"62373cssna00")
		else:
			self.personalInfo=Personal("Dummy",11,"unknown")
			self.bankAccount=BankAccount(99999999,"/////////")
		
	def getPersonal(self):
		return self.personalInfo	
	def getbankAccount(self):
	        return self.bankAccount
	


class Personal:

	def __init__ (self,n,a,ad):
		self.name=n
		self.age=a
		self.address=ad
	def getName(self):
		return self.name
	def getAge(self):
		return self.age
	def getAddress(self):
		return self.address
	def close(self):
		pass
	

class BankAccount:
	
	def __init__(self,I,B):
		self.IBAN=I
		self.BIC=B		
		self.Balance=Balance()
	def getIBAN(self):
		return self.IBAN
	def getBIC(self):
		return self.BIC
	def getBalance1(self):
	        return self.Balance
	def close(self):
		pass
	

class Balance:

	def __init__(self):
		self.Balance=1000
	def getBalance(self):
		return self.Balance
	def withdraw(self,x):
		self.Balance-=x
	        return self.Balance
	def deposit(self,y):
		self.Balance+=y
		return self.Balance
	def close(self):
		pass
	

	

