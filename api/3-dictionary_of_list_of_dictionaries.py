#!/usr/bin/python3
"""Python script to export data in the JSON format."""

from requests import get
import json

if __name__ == '__main__':
    url_one = get('https://jsonplaceholder.typicode.com/todos/')
    data_one = url_one.json()

    row = []
    url_two = get('https://jsonplaceholder.typicode.com/users/')
    data_two = url_two.json()

    new_dict = {}

    for j in data_two:
        row = []
        for i in data_one:
            new_dict2 = {}
            if j['id'] == i['userId']:
                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                row.append(new_dict2)
        new_dict[j['id']] = row

    with open("todo_all_employees.json", 'w') as file:
        json_obj = json.dumps(new_dict)
        file.write(json_obj)
