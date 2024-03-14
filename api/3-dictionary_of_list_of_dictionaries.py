#!/usr/bin/python3
"""module for dummy api manipulation"""
import csv
import json
from os import sys
import requests


if __name__ == "__main__":
    # setting base url
    base_url = "https://jsonplaceholder.typicode.com/"

    # requesting todos, converting to json object
    todos = requests.get(base_url + "todos/")
    j_todos = todos.json()

    # # requesting username and userId from employee object
    # username: str = j_employee.get("username")
    # userId: int = j_employee.get("id")

    # creating attributes, and csv fields, list of dictionaries
    attributes = ["username", "task", "completed"]
    user_tasks = []

    # getting a list of ids
    all_users = requests.get(base_url + "users/")
    j_all_users = all_users.json()

    user_list = []
    for user in j_all_users:
        user_list.append(user["id"])

    user_id_tasks = {}
    # getting all tasks linked to employee id in list of dict
    for user in user_list:
        for task in j_todos:
            if task["userId"] == int(user):
                employee = requests.get(base_url + "users/" + str(user))
                j_employee = employee.json()
                task["username"] = j_employee["username"]
                task["task"] = task["title"]
                d = {}
                for attr in attributes:
                    d.update({attr: task.get(attr)})
                user_tasks.append(d)
        user_id_tasks.update({f"{user}": user_tasks})

    with open(f"todo_all_employees.json", 'w') as file:
        json.dump(user_id_tasks, file)
