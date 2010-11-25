# To change this template, choose Tools | Templates
# and open the template in the editor.
class Money:
    def __init__(self,amount):
        self.amount = amount

    def times(self, multiplier):
        pass

    def dollar(self,amount):
        return Dollar(amount)

    def franc(self,amount):
        return Franc(amount)

    def __eq__(self,other):
        if isinstance(other, Money):
            return (self.__dict__==other.__dict__) and (self.__class__.__name__==other.__class__.__name__)
        return False

class Dollar(Money):
    def __init__(self,amount):
        self.amount = amount
    def times(self,multiplier):
        return Dollar(self.amount * multiplier)
    
class Franc(Money):
    def times(self,multiplier):
        return Franc(self.amount * multiplier)
    
