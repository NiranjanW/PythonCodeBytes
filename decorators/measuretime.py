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
 
# prints Function took 5.002753257751465 seconds to run
slow_function(5)