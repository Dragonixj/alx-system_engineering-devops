#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format
"""

import json
from sys import argv

from requests import get


def get_data(employee_id):
    BASE_URL = "https://jsonplaceholder.typicode.com"
    rq = get(BASE_URL + f"/users/{employee_id}")
    usr = rq.json()

    rq = get(BASE_URL + f"/users/{employee_id}/todos")
    todos = rq.json()
    task_list = []
    for todo in todos:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": usr["username"],
        }
        task_list.append(task)

    data = {str(usr["id"]): task_list}
    filename = f"{usr['id']}.json"
    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    get_data(argv[1])
