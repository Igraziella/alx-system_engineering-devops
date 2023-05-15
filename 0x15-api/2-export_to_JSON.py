#!/usr/bin/python3
""" Exports data from https://jsonplaceholder.typicode.com
    in the JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    """ Get the todo list progress of an employee """
    API = "https://jsonplaceholder.typicode.com"

    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(API, user_id)
    username = requests.get(user_endpoint).json().get("username")
    tasks_endpoint = "{}/todos".format(API)
    tasks = requests.get(tasks_endpoint).json()
    user_todos = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in tasks if task.get("userId") == user_id
        ]
    }

    # save in json file
    with open("{}.json".format(user_id), 'w', encoding="utf-8") as file:
        json.dump(user_todos, file)
