#!/usr/bin/python3
"""
Script uses a REST API to return info about an employee's TODO list progress
and exports the data to a CSV file.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
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

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    export_to_csv(employee_id)
