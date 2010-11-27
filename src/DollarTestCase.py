import unittest
from Dollar import Dollar
from Dollar import Franc
from Dollar import Money


class DollarTestCase(unittest.TestCase):

    def test_Multiplication(self):
        five = Money.dollar(5)
        self.assertEquals( Money.dollar(10), five.times(2), "5$*2==10$" )
        self.assertEquals( Money.dollar(15), five.times(3), "5$*3==15$" )

    def test_FrancMultiplication(self):
        five = Money.franc(5)
        self.assertEquals( Money.franc(10), five.times(2), "5$*2==10$" )
        self.assertEquals( Money.franc(15), five.times(3), "5$*3==15$" )

    def test_Equality(self):
        self.assertTrue(Dollar(5)==Dollar(5), "Dollar(5) must equal Dollar(5)")
        self.assertFalse(Dollar(5)==Dollar(6), "Dollar(5) must not equal Dollar(6)")
        self.assertTrue(Franc(5)==Franc(5), "Franc(5) must equal Franc(5)")
        self.assertFalse(Franc(5)==Franc(6), "Franc(5) must not equal Franc(6)")
        self.assertFalse(Dollar(5)==Franc(5), "Franc(5) must not equal Dollar(5)")

    def test_Currency(self):
        self.assertEqual("USD", Money.dollar(1).currency(), '"USD" == money.dollar(1).currency')
        self.assertEqual("CHF", Money.franc(1).currency(),  '"CHF" == money.franc(1).currency')

        