class CustomException(Exception):
    def __init__(self, message):
        super().__init__(self,message)


try:
    raise CustomException("This is a Custom Exception")   
except Exception as e:
    print(f"Caught an exception as {e}") 

class ZeroOneException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

try:
    raise ZeroOneException("This error occurs if divided by zero")
except Exception as e:
    print(f"Caught an Exception as {e}")