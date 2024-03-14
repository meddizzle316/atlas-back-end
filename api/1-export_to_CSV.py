#!/usr/bin/python3
"""module for dummy api manipulation"""
import csv
import json
from os import sys
import requests


if __name__ == "__main__":
    # setting base url
    base_url = "https://jsonplaceholder.typicode.com/"

    # getting Employee name using params passed to file
    id = sys.argv[1]

    # requesting user with given id and converting it to json object
    employee = requests.get(base_url + "users/" + id)
    j_employee = employee.json()

    # using "get" on json object to get name field
    e_name: str = j_employee.get("name")

    # requesting todos, converting to json object
    todos = requests.get(base_url + "todos/")
    j_todos = todos.json()

    # requesting username from employee object
    username: str = j_employee.get("username")

    # creating attributes, and csv fields, list of dictionaries
    attributes = ['userId', "username", "completed", "title"]
    user_tasks = []

    # getting all tasks linked to employee id in list of dict
    for task in j_todos:
        if task["userId"] == int(id):
            task["username"] = username
            d = {}
            for attr in attributes:
                d.update({attr: task.get(attr)})
            user_tasks.append(d)

    # converting user_tasks into csv file
    with open(f"{id}.csv", 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            csv_writer.writerow(task.values())
