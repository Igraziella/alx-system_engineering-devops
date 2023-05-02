#!/usr/bin/python3
"""  Exports data from "https://jsonplaceholder.typicode.com" in the CSV format.
"""
import csv
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
    user_todos = [todo for todo in todos if todo.get("userId")]

    with open('{}.csv'.format(userId), 'w') as file:
        for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            userId,
                            name,
                            todo.get('completed'),
                            todo.get('title')
                            )
                        )
