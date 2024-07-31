#!/usr/bin/python3
"""
This script fetches TODO list progress of an employee using a REST API
"""

import requests
import sys

if __name__ == "__main__":
    # Validate input arguments
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Validate if employee_id is an integer
    try:
        int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # API URLs
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_tds = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user data
    user = requests.get(url_user).json()
    employee_name = user.get('name')

    # Fetch tasks data
    todos = requests.get(url_tds).json()

    # Calculate task progress
    cmp_tasks = [todo.get('title') for todo in todos if todo.get('completed')]
    tl_tk = len(todos)
    dn_tasks = len(cmp_tasks)

    # Display the output
    print(f"Employee {employee_name} is done with tasks({dn_tasks}/{tl_tk}):")
    for task in cmp_tasks:
        print(f"\t {task}")

