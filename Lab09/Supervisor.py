#Author: Perfect-Princess Makuwerere
#Date: April 14, 2026
#Description: Defines the Supervisor subclass with an overridden calcPay method.

from Employee import Employee

class Supervisor(Employee):
    def __init__(self, name, id_number, pay_rate, level):
        super().__init__(name, id_number, pay_rate) 
        self.__level = level

    def calcPay(self, hours):
        """
        Overridden pay calculation including a level-based bonus.
        """
        base_pay = self._pay_rate * hours 
        bonus = 1000.00 * self.__level 
        return base_pay + bonus

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level 