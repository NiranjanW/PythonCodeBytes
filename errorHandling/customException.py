from enum import Enum, unique , auto
import sys

@unique
class ErrorCodes(Enum):
    
    ERR_INCORRECT_ERRCODE = "Unknow Error"  
    ERR_SITUATION_1 = auto()            # description of situation 1
    ERR_SITUATION_2 = auto()            # description of situation 2
    ERR_SITUATION_3 = auto()            # description of situation 3
    ERR_SITUATION_4 = auto()            # description of situation 4
    ERR_SITUATION_5 = auto()            # description of situation 5
    ERR_SITUATION_6 = auto()  # error code passed is not specified in enum ErrorCodes
    # 400510 = "Unsupported Media Type"           # description of situation 1
    # "500100" = "Not Implemented" 
    #       # description of situation 2
    # "400000" = "Invalid value 'XX_1234' for header trace-id. Expected min length 20 for value "        # description of situation 3
  
class CustomError(Exception) :
    
    def __init__(self,error_code , message='' , *args , **kwargs):
        
        if not isinstance(error_code,ErrorCodes):
            msg = 'Error code passed in the error_code param must be of type {0}'
            raise CustomError(ErrorCodes.ERR_INCORRECT_ERRCODE, msg, ErrorCodes.__class__.__name__)
        
        self.error_code = error_code
        
        self.traceback = sys.exc_info
        
        try:
             msg = '[{0}] {1}'.format(error_code.name, message.format(*args, **kwargs))
        except (IndexError, KeyError):
            msg = '[{0}] {1}'.format(error_code.name, message)

        super().__init__(msg)