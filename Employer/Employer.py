from itertools import groupby
from operator import itemgetter
import pprint
from Exception.Exception import StarlingEmployerDataNotLoadException

class Employer():
    def __init__(self):
        self.employee_data = None
        self.__loaded = False

    def load_employee_data(self):
        self.employee_data = [{'date': '2017-03-01', 'dept': 'Sales', 'employee': 3, 'salary': 70000},
             {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 4, 'salary': 45000},
             {'date': '2017-09-01', 'dept': 'Sales', 'employee': 4, 'salary': 60000},
             {'date': '2016-03-01', 'dept': 'Sales', 'employee': 5, 'salary': 40000},
             {'date': '2017-12-01', 'dept': 'Support', 'employee': 5, 'salary': 65000},
             {'date': '2016-02-01', 'dept': 'Support', 'employee': 5, 'salary': 40000},
             {'date': '2016-03-01', 'dept': 'Support', 'employee': 6, 'salary': 70000},
             {'date': '2016-11-01', 'dept': 'Engineering', 'employee': 6, 'salary': 45000},
             {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 7, 'salary': 70000},
             {'date': '2015-09-01', 'dept': 'Sales', 'employee': 7, 'salary': 55000},
             {'date': '2017-11-01', 'dept': 'Support', 'employee': 7, 'salary': 50000},
             {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 7, 'salary': 65000},
             {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 8, 'salary': 60000},
             {'date': '2017-11-01', 'dept': 'Sales', 'employee': 9, 'salary': 55000},
             {'date': '2015-01-01', 'dept': 'Support', 'employee': 9, 'salary': 55000},
             {'date': '2017-12-01', 'dept': 'Engineering', 'employee': 10, 'salary': 55000},
             {'date': '2016-12-01', 'dept': 'Sales', 'employee': 10, 'salary': 50000},
             {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 10, 'salary': 70000},
             {'date': '2016-11-01', 'dept': 'Support', 'employee': 11, 'salary': 75000},
             {'date': '2016-08-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
             {'date': '2016-06-01', 'dept': 'Engineering', 'employee': 12, 'salary': 40000},
             {'date': '2015-01-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
             {'date': '2015-11-01', 'dept': 'Support', 'employee': 12, 'salary': 45000},
             {'date': '2016-03-01', 'dept': 'Sales', 'employee': 13, 'salary': 60000},
             {'date': '2015-01-01', 'dept': 'Engineering', 'employee': 13, 'salary': 70000},
             {'date': '2017-08-01', 'dept': 'Engineering', 'employee': 13, 'salary': 75000},
             {'date': '2015-12-01', 'dept': 'Sales', 'employee': 14, 'salary': 60000},
             {'date': '2017-07-01', 'dept': 'Support', 'employee': 16, 'salary': 60000},
             {'date': '2016-12-01', 'dept': 'Engineering', 'employee': 17, 'salary': 45000},
             {'date': '2017-11-01', 'dept': 'Engineering', 'employee': 18, 'salary': 45000},
             {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 20, 'salary': 45000},
             {'date': '2016-06-01', 'dept': 'Sales', 'employee': 21, 'salary': 40000},
             {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 21, 'salary': 70000},
             {'date': '2016-01-01', 'dept': 'Engineering', 'employee': 23, 'salary': 50000},
             {'date': '2016-02-01', 'dept': 'Engineering', 'employee': 23, 'salary': 75000},
             {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 24, 'salary': 55000},
             {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 25, 'salary': 50000},
             {'date': '2017-05-01', 'dept': 'Sales', 'employee': 28, 'salary': 60000},
             {'date': '2017-10-01', 'dept': 'Support', 'employee': 29, 'salary': 40000},
             {'date': '2017-06-01', 'dept': 'Engineering', 'employee': 30, 'salary': 70000}]

        # self.__loaded = True

    def __validated_employee_data_loaded(self):
        if self.__loaded is False:
            raise StarlingEmployerDataNotLoadException("Employer data not loaded")


    def group_employees_by_attr(self, key):

        self.__validated_employee_data_loaded()

        sorted_employee_data = sorted(self.employee_data, key=key)

        grouping_by_attr = {}

        for k, g in groupby(sorted_employee_data, key=key):
            grouping_by_attr[k] = list(g)

        return grouping_by_attr

    @staticmethod
    def sum_by_attr(list_of_employees, attr):
        return sum(employee[attr] for employee in list_of_employees)

    def average_employee_data_by_grouping(self, key, attr):

        grouping_by_attr = self.group_employees_by_attr(key=key)

        avgs_by_attr = { k: self.sum_by_attr(list_of_employees, attr)/len(list_of_employees) for k, list_of_employees in grouping_by_attr.items()}

        return avgs_by_attr




