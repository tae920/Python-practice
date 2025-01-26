# A python program using classes and objects to manage employees
# Author : Taeseok LEE
# Date Created : 30/8/2021

from employee_management_system.employee_class import Employee

# subclass of the Employee class
class Contractor(Employee):
    def __init__(self, name, id, department, job_title, end_date, abn, salary):
        # Call the superclass's __init__ method and pass
        super().__init__(name, id, department, job_title)
        self.__end_date = end_date
        self.__abn = abn
        self.__salary = salary

# Accessors and mutators for this class
    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_abn(self, abn):
        self.__abn = abn

    def set_salary(self, salary):
        self.__salary = salary

    def get_end_date(self):
        return self.__end_date

    def get_abn(self):
        return self.__abn

    def get_salary(self):
        return self.__salary
