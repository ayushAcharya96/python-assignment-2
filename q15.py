'''
15. Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
'''

class Bank:
  @staticmethod
  def generate_account_no():
    return 'returns unique account no.'
  @staticmethod
  def transfer_money(sender_account_number, receiver_account_number, transfer_amount):
    return True

class Customer:
  def __init__(
    self,
    full_name,
    current_address,
    permanent_address,
    contact_no,
    father_name,
    mother_name,
    identification_document_type,
    identification_document,
    education_qualification,
    account_type,
    salary,
    balance
    ):
    self.full_name = full_name
    self.current_address = current_address
    self.permanent_address = permanent_address
    self.contact_no = contact_no
    self.father_name = father_name
    self.mother_name = mother_name
    self.identification_document_type = identification_document_type
    self.identification_document = identification_document
    self.education_qualification = education_qualification
    self.account_type = account_type
    self.salary = salary
    self.balance = balance
    self.account_no = Bank.generate_account_no()
    self.is_active = True
  
  def check_balance(self):
    return self.balance
  
  def deposit_money(self, deposite_amount):
    self.balance += deposite_amount
    return f'Your balance is {self.balance}'
  
  def withdraw_money(self, withdraw_amount):
    if withdraw_amount > self.balance:
      return 'Your balance is not sufficient.'
    else:
      return f'Rs.{withdraw_amount} has been withdrawm. Balance is {self.balance}'
  
  def transfer_money(self, transfer_amount, receiver_account_number):
    if transfer_amount > self.balance:
      return 'Your balance is not sufficient.'
    else:
      is_transfered = Bank.transfer_money(self.account_no, receiver_account_number, transfer_amount)
      if is_transfered:
        self.balance -= transfer_amount
        return f'Rs{transfer_amount} has been transfered to A/c no {receiver_account_number}. Your current balance is {self.balance}.'
      else:
        return 'Something went wrong. Please try again.'
  
  def deactivate_account(self):
    self.is_active = False
    return "Account deactivated."