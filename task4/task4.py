"""
Your task is to write a class maskify, which changes all but the last four characters into '#'.
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""


class must get input string in constructor and consists of 2 methods: public_value(), private_value()

public_value - return masked
private_value - return original
"""

class Maskify:
    """
    Changes all but the last four characters into '#'.
    """
    def __init__(self, input_string):
        """
        Not a Constructor, just a method for initializing an instance of the class
        """
        self.input_string = str(input_string)
        
    def private_value(self):
        return self.input_string
        
    def public_value(self):
        if len(self.input_string) <= 4:
            return self.input_string
        else:
            not_masked = self.input_string[-4:]
            masked = (len(self.input_string) - 4) * "#"
            return masked + not_masked
