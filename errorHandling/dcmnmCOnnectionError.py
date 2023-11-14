import logging
import functools

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DCNMConnectionError(Exception):
    def __init__(self, error_dict):
        self.error_dict = error_dict

    def __str__(self):
        return f'{self.error_dict}'


def handle_the_error(error):
    print(error)
    error = eval(str(error))
    if error['RETURN_CODE'] == '404':
        print(f'Path {error["REQUEST_PATH"]} does not exist. Please try a different path')


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
    raise DCNMConnectionError(_return_info(rc, method, path, msg, jrd))