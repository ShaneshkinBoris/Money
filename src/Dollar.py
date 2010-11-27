from abc import abstractmethod
# To change this template, choose Tools | Templates
# and open the template in the editor.
class Money:
    def __init__(self,amount):
        self.amount = amount
        self.currency = None

    def times(self, multiplier):
        pass
    
    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

    def currency(cls):
        return cls.currency

    def __eq__(self,other):
        if isinstance(other, Money):
            return (self.__dict__==other.__dict__) and (self.__class__.__name__==other.__class__.__name__)
        return False

class Dollar(Money):

    def __init__(self, amount):
        self.amount = amount
        self.currency = "USD"

    def times(self,multiplier):
        return Dollar(self.amount * multiplier)

    
class Franc(Money):

    def __init__(self, amount):
        self.amount = amount
        self.currency = "CHF"


    def times(self,multiplier):
        return Franc(self.amount * multiplier)

    
