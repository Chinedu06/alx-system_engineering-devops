#!/usr/bin/python3
"""
This script retrieves data from a given API and saves all tasks of all
employees in a JSON file named todo_all_employees.json.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    user_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = [task for task in todos if task.get('userId') == user_id]
        user_tasks[user_id] = [
            {"username": username, "task": task.get('title'),
             "completed": task.get('completed')} for task in tasks]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)
