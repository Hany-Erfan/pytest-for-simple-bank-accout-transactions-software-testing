from Bankaccount import Customer
import pytest

@pytest.fixture(scope="module")
def transaction():
	Jennifer=Customer(123)	
	jenibankAccount=Jennifer.getbankAccount()
	jenibalance=jenibankAccount.getBalance1()
	
	yield jenibalance			

	jenibalance.close()




def test_Balancetransactions(transaction):
	transaction.deposit(100)
	transaction.withdraw(30)
	amount =transaction.getBalance()
	print (amount)
	assert amount==1070

