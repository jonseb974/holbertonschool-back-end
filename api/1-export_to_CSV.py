#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
from sys import argv
import csv

if __name__ == '__main__':
    first = get('https://jsonplaceholder.typicode.com/todos/')
    data_one = first.json()

    row = []
    second = get()
    data_two = second.json('https://jsonplaceholder.typicode.com/users/')

    for todo in data_two:
        if todo['id'] == int(['id']):
            employee = todo['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        wrti = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in data_one:
            row = []
            if todo['userId'] == int(argv[1]):
                row.append(employee)
                row.append(todo['completed'])
                row.append(todo['title'])
                row.append(todo['userId'])
                wrti.writerow(row)
