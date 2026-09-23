class Demo:
    iValue1 = 10
    iValue2 = 11

    def __init__(self):

        print("Inside Constructor")
        self.iNo1 = 16
        self.iNo2 = 29

    def __del__(self):
        print("Inside Distructor")

    def fun(self):
        print("Inside Instance Method named as Fun")
        print(self.iNo1)
        print(self.iNo2)

        print(self.iValue1)
        print(self.iValue2)

obj1 = Demo()
obj1.fun()

