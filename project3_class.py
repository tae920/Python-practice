# A python program to follow tasks using ClockMain
# Author : Taeseok LEE
# Assessment : Assignment 2 Project 3
# Date Created : 30/8/2021

# Superclass for project 3 which holds general data
class Employee:
    def __init__(self, name, id, department, job_title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title

# Accessors and mutators for this class
    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def get_id(self):
        return self.__id

    def set_info(self, name, department, job_title):
        self.__name = name
        self.__department = department
        self.__job_title = job_title
