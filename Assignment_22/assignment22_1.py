class demo:

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print("Inside fun")
        print("Value of no1:", self.no1)
        print("Value of no1:", self.no2)
    def gun(self):
        print("Inside gun")
        print("Value of no1:", self.no1)
        print("Value of no1:", self.no2)

def main():

    obj1 = demo(10, 20)
    obj2 = demo(30, 40)
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()
    

if __name__ == "__main__":
    main()
