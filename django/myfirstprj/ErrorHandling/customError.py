class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("Calling str")
        if self.message:
            return "MuCustomEr , {0}".format(self.message)
        else:
            return "MyCustomError raised"

raise MyCustomError("Zero error raised")
