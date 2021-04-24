from datetime import datetime

now = datetime.now()

import random
import database
import validation
from getpass import getpass


print(now)
def init():

    print("Weclome to RP Bank")

    haveAccount = int(input("Do you have a bank account with us: 1 (yes) 2 (no) \n"))
  
    if haveAccount == 1:
        login()

  #don't have an account
    elif haveAccount == 2:
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")
        #makes password invisible
        user = database.authenticated_user(account_number_from_user, password);

        if user:
            auth_session_created = database.create_auth_session( account_number_from_user )
            bank_operation(user,  account_number_from_user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    
    print("***********Registeration***********")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n" )
    last_name = input("What is your last name? \n")
    password = getpass("Enter a new password \n")
    balance = int(input("How much money would you like to deposit? \n"))

    account_number = generation_account_number()
    
    is_user_created = database.create(account_number, first_name, last_name, email, password, balance) #str(0)
    #using database module to create new user record

    if is_user_created:
        print("Your Account Has been created \n")
        print("********************************")
        print("Your account number is %d" % account_number)
        print("********************************")
        
        login()
    else:
        print("Something went wrong, please try again")
        register()

def bank_operation(user, account_number_from_user):
    print("Welcome %s %s \n" % (user[0], user[1])) #user[0] = first name
  
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) log out (4) exit "))

    if(selectedOption == 1):
        depositOperation(user, account_number_from_user)

    elif(selectedOption == 2):
        withdrawalOperation(user, account_number_from_user)

    elif(selectedOption == 3):
        print("You have now logged out")
        logout(account_number_from_user)

    elif(selectedOption == 4):
        exit()

    else:
        print("Invalid option selected")
        bank_operation(user,  account_number_from_user)

def depositOperation(user, account_number_from_user):

#    current_balance = int(user[4])

    print("You have selected deposit")
    deposit = int(input ('How much would you like to deposit? \n'))
    new_balance = current_balance(user) + deposit

    set_new_balance(user, new_balance)
    database.update_user_record( account_number_from_user, user )
    database.update_auth_session( account_number_from_user, user )
    print ('The current balance is $ %d ' % new_balance)
    print ('\n')
    bank_operation(user, account_number_from_user)

def withdrawalOperation(user, account_number_from_user):
    print("You have selected withdrawal")
    #get current balance
    print("Your current balance is %d" % current_balance(user))
    cash = int(input('How much would you like to withdraw? \n'))
    new_withdrawn_balance = current_balance(user) - cash
    print("Your remaining balance is $ %d" % new_withdrawn_balance)
    print('Take your cash')
    print ('\n')

    set_new_balance(user, new_withdrawn_balance)
    database.update_user_record( account_number_from_user, user )
    database.update_auth_session( account_number_from_user, user )
    print ('The current balance is $ %d ' % new_withdrawn_balance)
    print ('\n')

    bank_operation(user, account_number_from_user)
    

def generation_account_number():
    return random.randrange(1111111111,9999999999)

def set_new_balance(user, balance):
    user[4] = balance


def current_balance(user):
    return int(user[4])

def logout(account_number_from_user ):
    database.delete(account_number_from_user)
    login()

init()
