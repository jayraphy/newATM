def account_number_validation(user_account_number):

    if user_account_number:

        try:
            int(user_account_number)

            if len(str(user_account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False