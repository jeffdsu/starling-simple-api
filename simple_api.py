import json

from flask import Flask

from Employer.Employer import Employer
from Response.Response import good_response, good_data_response, bad_response
from Exception.Exception import deal_with_exception


import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


app = Flask(__name__)

@app.route("/averages", methods=['GET'])
def get_employee_averages_by_dept():

    try:
        employer = Employer()
        employer.load_employee_data()

        averages = employer.average_employee_data_by_grouping(key=lambda employee: employee['dept'], attr='salary')

        return good_response(averages)

    except Exception as e:

        return deal_with_exception(e)


def convert_group_data_to_headcount_data(group_data):
    return [ {"month": k, "headcount": len(v)} for k, v in group_data.items()]

@app.route("/headcount_over_time", methods=['GET'])
def get_employee_headcount_over_time_by_date():

    try:
        employer = Employer()
        employer.load_employee_data()

        grouping_data = employer.group_employees_by_attr(key=lambda employee: employee['date'])

        headcount_data = convert_group_data_to_headcount_data(grouping_data)

        return good_data_response(headcount_data)

    except Exception as e:

        return deal_with_exception(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)