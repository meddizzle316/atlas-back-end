#!/usr/bin/python3
from os import sys
import requests
import json

# setting base url
base_url = "https://jsonplaceholder.typicode.com/"

#getting Employee name using params passed to file
id = sys.argv[1]
#making sure I got the right id
print(id)

#requesting user with given id and converting it to json object
employee = requests.get(base_url + "users/" + id)
j_employee = employee.json()
print(j_employee)
