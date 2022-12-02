#!/usr/bin/python3
"""Script to export Json Format data"""

from requests import get
from sys import argv
import json

if __name__ == '__main__':
    url_one = get('https://jsonplaceholder.typicode.com/todos/')
    data_one = url_one.json()

    row = []
    url_two = get('https://jsonplaceholder.typicode.com/users/')
    data_two = url_two.json()

    for item in data_two:
        if item['id'] == int(argv[1]):
            employee = item['username']
            id_nb = item['id']

    row = []

    for item in data_one:
        new_dict = {}
        if item['usersId'] == int(argv[1]):
            new_dict['username'] = employee
            new_dict['task'] = item['title']
            new_dict['completed'] = item['completed']
            row.append(new_dict)

    full_dict = {}
    full_dict[id_nb] = row
    json_obj = json.dumps(full_dict)

    with open(argv[1] + '.json', 'w') as file:
        file.write(json_obj)
