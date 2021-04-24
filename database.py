#create record
#update reccord
#read record
#delete record
#CRUD

#find user

import os
import validation

user_db_path = "data/user_record/"
auth_session_path = "data/auth_session/"

def create(user_account_number, first_name, last_name, email, password, balance):

 # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(balance)

    if does_account_number_exist(user_account_number):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False
    try:
        f= open(user_db_path + str(user_account_number) + ".txt", "x")
    
    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
    
    else: #in 'try' I'm trying to create a file, if there are no errors 'except', then I'm going to come here

        f.write(str(user_data))
        completion_state = True
    
    #everything in finally will always run
    finally: 
        f.close()
        return completion_state

        # def account_number_validation(account_number):
        #     if account_number:
        #         if len(str(account_number)) == 10:
        #             try:
        #                 int(account_number) #if we can convert the account number to integer
        #                 return True

        #             except ValueError:
        #                 print("Invalid Account number, account number should be integer")
        #                 return False
        #             except TypeError:
        #                 print("Invalid account type")
        #                 return False

        #         else:
        #             print("Account Number cannot be less or more than 10 digits")
        #             return False
        #     else:
        #         print("Account Number is a required field")
        #         return False #this validation failed
        
def read(user_account_number):
    #find user with account number
    #fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if user_account_number: #is__account_number:
            f= open(user_db_path + str(user_account_number) + ".txt", "r")
        else: 
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid account number format")
    
    else:
        return f.readline() #only needs to read the first line

def update(user_account_number):
    print("update user record")
    #find user with account number
    #fetch the content of the file
    #update the content of the file
    #save the file
    #return true

def delete(user_account_number):

    #find user with account number
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number)+ ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number)+ ".txt")
            is_delete_successful = True

        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_successful

    #delete the user record(file)
    #return true

def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + ".txt":

            return True

    return False

def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False

def update_user_record( user_account_number, user ):
    current_balance = user[4]
    
    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    f = open(user_db_path + str(user_account_number) + ".txt", "w")
    f.write(updated_user)
    f.close()


def create_auth_session( user_account_number ):
        duplicated_user_record_file = open(user_db_path + str(user_account_number) + ".txt").read()
        f = open(auth_session_path + str(user_account_number) + ".txt", "x")
        f.write(str(duplicated_user_record_file));

def update_auth_session( user_account_number, user ):
    print("Update user record")
    current_balance = user[4]
    
    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    f = open(auth_session_path + str(user_account_number) + ".txt", "w")
    f.write(updated_user)
    f.close()


