import json
import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['username']

    # Get TODO list for the employee
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()

    # Prepare data
    user_data = []
    for task in todo_data:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        user_data.append(task_info)

    # Write data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump({employee_id: user_data}, file, indent=4)
    print(f"JSON file '{filename}' has been created successfully.")

if name == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)