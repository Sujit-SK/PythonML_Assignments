class bankAccount:
    # Class variable
    ROI = 10.5   
    def __init__(self, name, amount):
        # Instance variables
        self.name = name
        self.amount = amount
       

    def display(self):
        print("Account Holder:", self.name)
        print("Account Balance:", self.amount)

    def deposit(self):
        no = int(input("Enter amount to deposit: "))
        self.amount += no
       
    def withdraw(self):
        no = int(input("Enter amount to withdraw: "))
        if no <= self.amount:
            self.amount -= no
        else:
            print("Insufficient balance")
    
    def calculate_interest(self):
        interest = (self.amount * bankAccount.ROI) / 100
        print(f" Interest: {interest}")
       

    

def main():

    name = input("Enter account holder name: ")
    amount = int(input("Enter initial amount: "))
    # Create first object
    obj1 = bankAccount(name,amount)

    obj1.display()
    obj1.deposit()
    obj1.display()
    obj1.withdraw()
    obj1.display()
    obj1.calculate_interest()


    name = input("Enter account holder name: ")
    amount = int(input("Enter initial amount: "))
    # Create first object
    obj2 = bankAccount(name,amount)

    obj2.display()
    obj2.deposit()
    obj2.display()
    obj2.withdraw()
    obj2.display()
    obj2.calculate_interest()

if __name__ == "__main__":
    main()