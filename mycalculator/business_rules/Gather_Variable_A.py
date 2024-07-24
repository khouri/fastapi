# import pandas as pd
# import numpy as np


class Gather_Variable_A:

    def __init__(self):
        className = type(self).__name__
        print(className)
    pass

    def get_variable_A(self, valor_entrada:int) -> str:

        my_variable = None
        if valor_entrada == 1:
            my_variable = "A"
        elif valor_entrada == 2:
            my_variable = "B"
        elif valor_entrada == 3:
            my_variable = "C"

        return(my_variable)
    pass

pass
