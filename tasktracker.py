import json
import os

file_path = r"C:\Users\miste\Task Tracker CLI\taskdata.json"

if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
    print("File exists and is readable")
    with open(file_path, 'r') as file:
        tasklist = json.load(file)
else:
    print("File does not exist, creating file")
    with open(file_path, 'w') as file:
        json.dump({}, file)
    tasklist = file

flag = True
while flag == True:

    print("This is the task tracker")
    print("Select an option:"
        "\n1. add"
        "\n2. update"
        "\n3. delete"
        "\n4. mark-in-progress"
        "\n5. mark-done"
        "\n6. list"
        "\n7. exit")

    option = input(">")
    if option == "exit":
        flag = False