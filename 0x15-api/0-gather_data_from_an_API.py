#!/usr/bin/python3
"""Script that gathers employee data from API:
    Returns to-do list info for a given employee id
"""
from sys import argv

from requests import get

if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    BASE_URL = "https://jsonplaceholder.typicode.com"

    employee = get("{}/users/{}".format(BASE_URL, employee_id)).json()
    todos = get(BASE_URL + "todos", params={"userId": argv[1]}).json()

    completed = get(
        "{}/users/{}todos?completed=true".format(BASE_URL, employee_id)
    ).json()

    print(
        "Employee {} is done with tasks({}/{})".format(
            employee.get("name"), len(completed), len(todos)
        ),
        *[t.get("title") for t in completed],
        sep="\n\t "
    )
