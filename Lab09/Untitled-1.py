# Author: Perfect-Princess Makuwerere
# Date: April 14, 2026
# Description: Defines the Employee superclass with protected members and pay calculation.

class Employee:
    def __init__(self, name, id_number, pay_rate):
        """
        Constructor for the Employee class.
        :param name: Name of the employee
        :type name: str
        :param id_number: ID number of the employee
        :type id_number: str
        :param pay_rate: Hourly pay rate
        :type pay_rate: float
        """
        self._name = name [cite: 35]
        self._id_number = id_number [cite: 36]
        self._pay_rate = pay_rate [cite: 37]

    def calcPay(self, hours):
        """
        Calculates the gross pay based on hours worked. [cite: 39]
        :param hours: Total hours worked
        :type hours: float
        :return: Total pay
        """
        return hours * self._pay_rate [cite: 39]

    # Getters and Setters [cite: 40]
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_id_number(self):
        return self._id_number

    def set_id_number(self, id_number):
        self._id_number = id_number

    def get_pay_rate(self):
        return self._pay_rate

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate