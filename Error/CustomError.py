class CustomError(TypeError):
    """
    This raised an error
    """
    def __init__(self, message, code):
        super().__init__(f"Error code: {code}, {message}")
        self.code = code


err = CustomError("Database breaks", 500)
print(err.__doc__)
