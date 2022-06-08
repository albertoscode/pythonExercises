
#examples of lambda with one argument

"""x = lambda checking_account_1: checking_account_1 * 0.3

print(x(1500))"""



"""x = lambda checking_account_1: checking_account_1 + 1200

print(x(1500))"""

#example of lambda with two arguments

"""x = lambda checking_account_1, saving_account: checking_account_1 * 0.3 + saving_account

print(x(1500, 2000))"""


#Example of lambda within a function with an argument

def savings(interest_rate):
    return lambda saving_account: saving_account * interest_rate

earned_interest = savings(.15)

print(earned_interest(1500))




    
