import csv
import json
import requests
import sys
import os

def export_todo_all_employees():
    # Get list of users
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Get TODO list for the user
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
        todo_data = todo_response.json()

        # Write data to CSV file
        filename = f"{user_id}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todo_data:
                writer.writerow([user_id, username, task['completed'], task['title']])
        print(f"CSV file '{filename}' has been created successfully.")

def user_info(id):
    filename = str(id) + ".csv"
    if not os.path.exists(filename):
        print(f"Number of tasks in CSV: 0")
    else:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            num_tasks = sum(1 for row in reader) - 1  # Subtract 1 to exclude header row
        print(f"Number of tasks in CSV: {num_tasks} (OK)")

if name == "__main__":
    if len(sys.argv) == 1:
        export_todo_all_employees()
    elif len(sys.argv) == 2:
        user_info(int(sys.argv[1]))
    else:
        print("Usage: python script.py <optional: employee_id>")