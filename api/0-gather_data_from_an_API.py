#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url_one = get('https://jsonplaceholder.typicode.com/todos/')
    data_one = url_one.json()
    completed = 0
    total = 0
    nb_task = []

    url_two = get('https://jsonplaceholder.typicode.com/users/')
    data_two = url_two.json()

    for i in data_two:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in data_one:
        if i.get('userId') == int(argv[1]):
            total += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee, completed, total))

    for i in nb_task:
        print("\t {}".format(i))
