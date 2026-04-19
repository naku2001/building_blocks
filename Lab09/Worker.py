#Author: Perfect-Princess Makuwerere
#Date: April 14, 2026
#Description: Defines the Worker subclass that inherits from Employee.

from Employee import Employee

class Worker(Employee):
    def __init__(self, name, id_number, pay_rate, shift):
        """
        Constructor for the Worker class.
        :param shift: 1 for day shift, 2 for night shift
        """
        super().__init__(name, id_number, pay_rate) 
        self.__shift = shift 

    def get_shift(self):
        return self.__shift

    def set_shift(self, shift):
        self.__shift = shift 