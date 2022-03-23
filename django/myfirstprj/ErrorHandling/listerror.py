# Do you raise or return errors in Python
# The raise statement allows the programmer to force a specific exception to occur. (8.4 Raising Exceptions)
# Use raise when you know you want a specific behavior, such as:



from typing import Union

lst = [1,2,3]


def divide(l , d):
    ans = 0
    try:
        ans = (l//d)
           
    except ( ZeroDivisionError, ValueError):
         raise 
        
    return ans

def main():
    div = [1,0]
    for i in lst:
        for d in div:
            result = divide(i ,1)
            continue
        print(result)

def share_sandwich(sandwich: int) -> Union[float, Exception]:
    try:
        bad_math = sandwich / 0
        return bad_math
    except Exception as e:
        return e

if __name__ == '__main__':
    main()