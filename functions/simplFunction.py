from typing import List


shopping_list = {
    "Bread" :1,
    "Butter" :2,
    "Milk" : 1,
    "Eggs" : 12
}

def show_list():

    for item , qty in shopping_list.items():
        print (f"{qty} x {item}")

# show_list()

def show_list_dict(lst:List)->None:
    for item , qty in lst.items():
         print (f"{qty} x {item}")

show_list_dict(shopping_list)         