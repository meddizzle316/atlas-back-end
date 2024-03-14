#!/usr/bin/python3
from os import sys
import requests
import json

# setting base url
base_url = "https://jsonplaceholder.typicode.com/"

#getting Employee name using params passed to file
id = sys.argv[1]
#making sure I got the right id
# print(id)

#requesting user with given id and converting it to json object
employee = requests.get(base_url + "users/" + id)
j_employee = employee.json()

#print out json employee object to make sure it worked
# print(j_employee)

#using "get" on json object to get name field
EMPLOYEE_NAME:str = j_employee.get("name")

#checking previous operation
# print(EMPLOYEE_NAME)

# requesting todos, converting to json object
todos = requests.get(base_url + "todos/")
j_todos = todos.json()

# printing json object
# print(j_todos)
#initializing count 
total_tasks = 0

#getting total tasks assigned to employee
for task in j_todos:
    if task["userId"] == int(id):
        total_tasks += 1

#checking total_tasks operation
# print(total_tasks)


#initializing count
completed_tasks = 0
completed_task_list = []

for task in j_todos:
    if task["userId"] == int(id) and task["completed"] == True:
        completed_tasks += 1
        completed_task_list.append(task["title"])

completed_task_list.insert(0, f"Employee {EMPLOYEE_NAME} is done with tasks({completed_tasks}/{total_tasks}):")

# print(completed_tasks)
print(*completed_task_list, sep='\n\t')
