# Decorators are a great way to add some meta programming to your code. They can extend the functions you already have and add new functionalities to then.

# They are heavily used on some frameworks as a way to make it easier for developers to implement common functionalities while keeping the code clean.
class Controller:
    def require_Admin(func):
#         def inner (*arg , **kwargs):
#             # the code for is_admin is suppressed due to NDA
#             if AuthorizationService.is_admin:
#                 return func(*args, **kwargs)
#             return '', 401
 
# # on the controller
# from Controller import requires_admin
 
# @requires_admin
# def get(query):
#     return service.get(**query), 200