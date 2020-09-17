import math

#Giving the user a choice between investment and bond (making everything capitalised so users input is not case sensitive)
print("Please choose either 'investment' or 'bond' from  from the menu below to proceed: ")
print("\n")
print("investment - to calculate the amount of interest you'll earn on interest \nbond - to calculate the amount you'll have to pay on a home loan")
print("\n")
investment_type = input("Enter here: ").upper()

#Asking for further input based on users choice + error message
#If the user chooses investment; give the user a choice between 'simple' and 'compound' 
if invest_type == "INVESTMENT":
    dep_amount = float(input("How much money will you be depositing? "))
    int_rate = float(input("Please enter the interest rate: "))
    num_years = float(input("How many years would you like to invest for? "))
    int_type = input("Would you like simple or compound interest? ")
    int_percent = int_rate / 100
    
    if int_type == "simple":
                simp_total = round(dep_amount * ( 1 + int_percent * num_years),2)
                print("Your total will be: R" + str(simp_total) + " which is: R" + str((simp_total-dep_amount)) + " more than you started with.")
         
    elif int_type == "compound":
                comp_total = round(dep_amount * math.pow((1 + int_percent), num_years),2)
                print("Your total will be: R" + str(comp_total) + " which is: R" + str((comp_total-dep_amount)) + " more than you started with.")

#If user chooses bond calculate the monthly amount the user will have to pay back
elif invest_type == "BOND":
    pres_value = float(input("What is the present value of the house? "))
    int_rate = float(input("Please enter the interest rate: "))                   
    num_months = float(input("How many months do you plan to take to repay the bond? "))
    int_percent = int_rate / 100
    mon_int = (int_percent / 12)
    repay = round((mon_int * pres_value ) / (1 - math.pow((1 + mon_int), (- num_months))),2)
    print("You will need to pay back R" + str(repay) + " each month.")

#If user puts neither investment nor bond give an error message
else:
    print("Sorry invalid input, please choose between 'investment' or 'bond'")
    
