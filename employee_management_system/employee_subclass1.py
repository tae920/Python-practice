# A python program using classes and objects to manage employees
# Author : Taeseok LEE
# Date Created : 30/8/2021

from employee_management_system.employee_class import Employee

# subclass of the Employee class
class ShiftEmployee(Employee):
    def __init__(self, name, id, department, job_title, shift_num, pay_rate):
        # Call the superclass's __init__ method and pass
        super().__init__(name, id, department, job_title)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

# Accessors and mutators for this class
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rate(self):
        return self.__pay_rate
