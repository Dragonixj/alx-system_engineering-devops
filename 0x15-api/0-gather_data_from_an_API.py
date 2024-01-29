#!/usr/bin/python3
"""Script that gathers employee data from API:
    Returns to-do list info for a given employee id
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    BASE_URL = "https://jsonplaceholder.typicode.com"
    rq = get(BASE_URL + f"/users/{employee_id}").json()

    todos = get(BASE_URL + f"/todos?userId={employee_id}").json()

    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            rq.get("name"), len(completed), len(todos)
        )
    )
    for task in completed:
        print("\t {}".format(task))
