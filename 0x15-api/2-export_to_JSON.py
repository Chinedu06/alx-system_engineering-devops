#!/usr/bin/python3
"""
This script uses a REST API to return information about an employee's TODO list
progress and exports the data to a JSON file.
"""
import json
import requests
import sys


def export_to_json(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    td_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(td_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        return

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")

    tasks = []
    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks.append(task)

    data = {str(employee_id): tasks}

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    export_to_json(employee_id)
