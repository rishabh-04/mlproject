# handling

import sys #sys library -- provides runtimeerrorinfo +various fns and variables also used in exception handling#
import logging
def error_message_detail(error,error_detail:sys):#error - object, error_detail - sys module
    _,_,exc_tb = error_detail.exc_info()
    #  which line which file exception has occured --> exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
      file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message
#above fn creates detailed error messages - file+line+error text#
 #file_name file where error occured , lineno str error - converts the exception to text#
#below fn - create exception type
class CustomException(Exception): #creating our own custion exception inherited from exception class#
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)