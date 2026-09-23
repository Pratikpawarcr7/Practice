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

        print(Demo.iValue1)
        print(Demo.iValue2)

    @classmethod
    def gun(cls):
        print("Inside Class Method")
#        print(Demo.iNo1)
#        print(Demo.iNo2)
        print(cls.iValue1)
        print(cls.iValue2)


    @staticmethod
    def sun():
            print("Inside Static Methon named as sun : ")
          
            print(Demo.Value1)
            print(Demo.Value2)
    
Demo.sun()


