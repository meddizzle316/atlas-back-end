#!/usr/bin/python3
"""module for dummy api manipulation"""
import json
import requests
from os import sys


if __name__ == "__main__":
    # setting base url
    base_url = "https://jsonplaceholder.typicode.com/"

    # getting Employee name using params passed to file
    id = sys.argv[1]
    # making sure I got the right id
    # print(id)

    # requesting user with given id and converting it to json object
    employee = requests.get(base_url + "users/" + id)
    j_employee = employee.json()

    # print out json employee object to make sure it worked
    # print(j_employee)

    # using "get" on json object to get name field
    e_name: str = j_employee.get("name")

    # checking previous operation
    # print(e_name)

    # requesting todos, converting to json object
    todos = requests.get(base_url + "todos/")
    j_todos = todos.json()

    # printing json object
    # print(j_todos)
    # initializing count
    total = 0

    # getting total tasks assigned to employee
    for task in j_todos:
        if task["userId"] == int(id):
            total += 1

    # checking total operation
    # print(total)
    # initializing count
    c_tasks = 0
    completed_task_list = []

    for task in j_todos:
        if task["userId"] == int(id) and task["completed"] is True:
            c_tasks += 1
            completed_task_list.append(task["title"])

    f_line: str = f"Employee {e_name} is done with tasks({c_tasks}/{total}):"
    completed_task_list.insert(0, f_line)

    # print(c_tasks)
    print(*completed_task_list, sep='\n\t')
