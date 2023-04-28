#!/usr/bin/python3
""" A script that, using https://jsonplaceholder.typicode.com,
    for a given employee ID, returns information about his/her
    TODO list progress.
"""
import sys
import requests


if __name__ == '__main__':
    """ Get the todo list progress of an employee """
    API = "https://jsonplaceholder.typicode.com"
    userId = int(sys.argv[1])
    user_endPoint = "{}/users/{}".format(API, userId)
    user_name = requests.get(user_endPoint).json().get("name")
    todos_endPoint = "{}/todos".format(API)
    todos = requests.get(todos_endPoint).json()
    todos_user = [dict for todo in todos if todo.get("user.Id")]

    # Count the number of completed tasks
    completed_todos = sum(todo['completed'] for todo in todos)

    # Display the progress
    total_tasks = len(todos)
    print("Employee {} is done with tasks({}/{})".format(
                        user_name, completed_todos, total_tasks))
    for todo in todos:
        if todo['completed']:
            print("\t  {}".format(todo['title']))
