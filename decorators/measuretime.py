import time

def measure_time(func):
   


    def wrapper (*arg):
        t = time.time()
        res = func(*arg)
        print(f"Function took {str(time.time()-t)} seconds to run")
        return res

    return wrapper

@measure_time
def slow_function(t):
    time.sleep(t)

def logging_func(orinal_func):
        def wrapper ( *args, **kwargs):
            print(f"called {orinal_func.__name__} with", args, kwargs)
            return orinal_func(*args, **kwargs)
        return wrapper

@logging_func
def add ( a,b):
    return a + b

 
# prints Function took 5.002753257751465 seconds to run
slow_function(5)