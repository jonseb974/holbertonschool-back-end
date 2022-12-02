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
    second = get('https://jsonplaceholder.typicode.com/users/')
    data_two = second.json()

    for i in data_two:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        wrti = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data_one:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])
                wrti.writerow(row)
