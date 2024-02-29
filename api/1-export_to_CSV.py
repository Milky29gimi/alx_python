import csv
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

    # Write data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])
    print(f"CSV file '{filename}' has been created successfully.")

if name == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)