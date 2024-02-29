import csv
import requests

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

if name == "__main__":
    export_todo_all_employees()