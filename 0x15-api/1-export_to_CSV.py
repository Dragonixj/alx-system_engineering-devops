#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format
"""

import csv
from sys import argv

from requests import get


def get_data(employee_id):
    BASE_URL = "https://jsonplaceholder.typicode.com"
    rq = get(BASE_URL + f"/users/{employee_id}")
    usr = rq.json()

    rq = get(BASE_URL + f"/users/{employee_id}/todos")
    todos = rq.json()

    filename = f"{usr['id']}.csv"
    with open(filename, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [usr["id"], usr["username"], todo["completed"], todo["title"]]
            )


if __name__ == "__main__":
    get_data(argv[1])
