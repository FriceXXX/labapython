class CalcError(Exception):
    def __init__(self, expression):
        super().__init__(expression)
