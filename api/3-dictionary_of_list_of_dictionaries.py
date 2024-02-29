import json
import requests

def get_todo_all_employees():
    # Initialize dictionary to store data for all employees
    all_employees_data = {}

    # Get list of users
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    # Iterate over each user
    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Get TODO list for the user
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
        todo_data = todo_response.json()

        # Prepare data for the user
        user_tasks = []
        for task in todo_data:
            task_info = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            user_tasks.append(task_info)

        # Store data for the user in the dictionary
        all_employees_data[user_id] = user_tasks

    # Write data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(all_employees_data, file, indent=4)
    print(f"JSON file '{filename}' has been created successfully.")

if name == "__main__":
    get_todo_all_employees()