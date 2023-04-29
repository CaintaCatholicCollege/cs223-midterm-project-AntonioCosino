#Antonio Miguel E. Cosino BSCS 2 A
import sys

correct_pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin != correct_pin:
    print("Invalid PIN. Program exiting.")
    sys.exit()

done = False
balance = 0

while not done:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = int(input("\nEnter choice: "))

    if choice == 1:
        deposit_amount = int(input("\nEnter amount to deposit: "))
        balance += deposit_amount
        print("Deposited {}. Current balance is {}.".format(deposit_amount, balance))
    elif choice == 2:
        withdraw_amount = int(input("\nEnter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient funds. Cannot withdraw.")
        else:
            balance -= withdraw_amount
            print("Withdrawn {}. Current balance is {}.".format(withdraw_amount, balance))
    elif choice == 3:
        print("\nCurrent balance is {}.".format(balance))
    elif choice == 4:
        done = True
    else:
        print("\nInvalid choice. Please try again.")

print("\nThank you for using the ATM. Program exiting.")
