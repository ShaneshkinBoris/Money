import unittest
from Dollar import Dollar
from Dollar import Franc
from Dollar import Money


class DollarTestCase(unittest.TestCase):

    def test_Multiplication(self):
        #todo: static
        money = Money(5)
        five = money.dollar(5)
        self.assertEquals( money.dollar(10), five.times(2), "5$*2==10$" )
        self.assertEquals( money.dollar(15), five.times(3), "5$*3==15$" )

    def test_FrancMultiplication(self):
        #todo: static
        money = Money(5)
        five = Franc(5)
        self.assertEquals( money.franc(10), five.times(2), "5$*2==10$" )
        self.assertEquals( money.franc(15), five.times(3), "5$*3==15$" )

    def test_Equality(self):
       self.assertTrue(Dollar(5)==Dollar(5), "Dollar(5) must equal Dollar(5)")
       self.assertFalse(Dollar(5)==Dollar(6), "Dollar(5) must not equal Dollar(6)")
       self.assertTrue(Franc(5)==Franc(5), "Franc(5) must equal Franc(5)")
       self.assertFalse(Franc(5)==Franc(6), "Franc(5) must not equal Franc(6)")
       self.assertFalse(Dollar(5)==Franc(5), "Franc(5) must not equal Dollar(5)")

    def test_Currency(self):
        #todo: static
        money = Money(5)
        self.assertEqual("USD", money.dollar(1).currency(), '"USD" == money.dollar(1).currency')
        self.assertEqual("CHF", money.franc(1).currency(), '"CHF" == money.franc(1).currency')

        