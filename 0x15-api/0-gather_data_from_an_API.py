#!/usr/bin/python3
""" A script that, using https://jsonplaceholder.typicode.com,
    for a given employee ID, returns information about his/her
    TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    """ Get the todo list progress of an employee """
    API = "https://jsonplaceholder.typicode.com"

    userId = int(sys.argv[1])
    user_endPoint = "{}/users/{}".format(API, userId)
    name = requests.get(user_endPoint).json().get("name")
    todos_endPoint = "{}/todos".format(API)
    todos = requests.get(todos_endPoint).json()
    user_todos = [todo for todo in todos if todo.get("userId") == userId]

    # Count the number of completed tasks
    completed_todos = [todo for todo in user_todos if todo.get("completed")]

    # Display the progress
    print("Employee {} is done with tasks({}/{}):".format(
                        name, len(completed_todos), len(user_todos)))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
