import functools
import logging

logger = logging.getLogger(__name__)


class DCNMConnectionError(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs['MESSAGE']
        self.rc = kwargs['RETURN_CODE']
        self.path = kwargs['REQUEST_PATH']
        self.method = kwargs['METHOD']
        self.data = kwargs['DATA']

    def __str__(self):
        return f'DCNM Connection Error Attempting to Connect to {self.path} Using {self.method}: ' \
               f'Received Return Code {self.rc} and Message {self.message}. Data Returned: {self.data}. '


def handle_the_error(error):
    print(error)
    print('Please try a different path')


def error_handler(msg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            value = None
            try:
                value = func(*args, **kwargs)
            except (DCNMServerResponseError, DCNMConnectionError) as e:
                logger.debug(f"e: {e}")
                logger.critical("{} - {}".format(msg, e))
                handle_the_error(e)
            return value
        return wrapper_decorator
    return decorator


@error_handler("this is and error tester")
def raise_error(rc, method, path, msg, jrd=None):
    # raise DCNMServerResponseError(_return_info(rc, method, path, msg, jrd))
    raise DCNMConnectionError(**_return_info(rc, method, path, msg, jrd))

def error_handler(msg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
            except (DCNMServerResponseError, DCNMConnectionError) as e:
                logger.debug(f"e: {e}")
                logger.critical("{} - {}".format(msg, e))
                raise
            return value

        return wrapper_decorator

    return decorator