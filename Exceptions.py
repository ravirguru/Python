class CustomException(Exception):
    def __init__(self, message):
        super().__init__(self,message)


try:
    raise CustomException("This is a Custom Exception")   
except Exception as e:
    print(f"Caught an exception as {e}") 
