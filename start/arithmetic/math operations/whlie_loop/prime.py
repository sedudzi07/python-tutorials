account_balance = 1000

amount_to_withdraw = float(input("Enter the amount you wanna withdraw: "))



if amount_to_withdraw > account_balance:
    print("Insufficint funds")
    print("Your account balance is: " ,(account_balance))
    print("you need to withdraw exact amount or less than the amount")
   




elif amount_to_withdraw <= account_balance:
    print("Successful transaction")
    print("Your new account balance is: ", account_balance - amount_to_withdraw)

    print("Thank you")