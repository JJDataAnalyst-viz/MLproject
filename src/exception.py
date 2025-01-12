import sys 
from logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    message_error = 'Error occured in Python script name [{0}] linie [{1}] message error [{2}]'.format(
        file_name,
        exec_tb.tb_lineno,
        str(error)
    ) 
    return message_error


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    



