import traceback
import logging
import sys

def zeroError (a :int , b :int) -> int :
    try:
        res = a/b 
    except ZeroDivisionError as exc:
        traceback.print_stack()
        # raise Exception("foo occurred").with_traceback(exc)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # traceback.format_tb(exc_type, exc_value, exc_traceback,
                            #   limit=2, file=sys.stdout)
        tb_str = traceback.format_exception(etype=type(exc_type), value=exc_value, tb=exc_traceback)
        print(tb_str)
        # traceback.print_exc()
        # print(traceback.format_exc()) 


if __name__ == "__main__" :
    logging.basicConfig(level=logging.DEBUG)
    x = zeroError( 1,0)
    logging.debug("%s " ,x)