#!/usr/bin/python3
""" A script that, using https://jsonplaceholder.typicode.com,
    for a given employee ID, returns information about his/her
    TODO list progress and exports the data in JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    """ Get the todo list progress of all employees
    and export data in JSON format
    """
    API = "https://jsonplaceholder.typicode.com"

    user_endpoint = "{}/users".format(API)
    users = requests.get(user_endpoint).json()
    tasks_endpoint = "{}/todos".format(API)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {user.get("id"): [{"username": user.get("username"),
                                    "task": task.get("title"),
                                    "completed": task.get("completed")}
                                   for task in tasks
                                   if task.get("userId") == user.get("id")]
                  for user in users
                }

    with open("todo_all_employees.json", 'w', encoding="utf-8") as file:
        json.dump(user_tasks, file)

