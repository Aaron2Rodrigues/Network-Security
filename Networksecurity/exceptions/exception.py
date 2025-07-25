import sys
from Networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
       self.error_message = error_message
       _,_,exc_tb = error_details.exc_info()

       self.lineno=exc_tb.tb_lineno
       self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] with error message [{2}]".format(
            self.filename, self.lineno, str(self.error_message)
    )



if __name__ == "__main__":
    try: 
        logging.info("Enter the try block")
        a=1/0
        print("This will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e, sys) 