
class MyException(BaseException):
    def __init__(self,message):
        self.message = message

    def displayMyError(self):
        print("This is MyException Error")
        print(self.message)